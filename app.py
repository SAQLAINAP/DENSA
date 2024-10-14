import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import logging
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'
db = SQLAlchemy(app)

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Mail configuration
class Config:
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() == 'true'
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

app.config.from_object(Config)
mail = Mail(app)

# Scheduler configuration
scheduler = BackgroundScheduler()

def send_email(recipient_email, news_headlines):
    msg = Message('Daily News', sender=app.config['MAIL_USERNAME'], recipients=[recipient_email])
    
    # Create HTML content for the email
    html_content = f"""
    <html>
        <body>
            <h1>Today's News Headlines</h1>
            <ul>
                {''.join(f'<li>{headline}</li>' for headline in news_headlines)}
            </ul>
        </body>
    </html>
    """
    
    msg.html = html_content
    
    # Attach the headlines.txt file
    with app.open_resource('headlines.txt') as att:
        msg.attach('headlines.txt', 'text/plain', att.read())
    
    try:
        mail.send(msg)
        logging.info(f"Email sent to {recipient_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")

def scrape_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find headlines (using h3 tags for BBC news)
            headlines = soup.find_all('h2')
            news_headlines = []
            
            for headline in headlines[:30]:  # Top 10 headlines
                headline_text = headline.get_text().strip()
                if headline_text:
                    news_headlines.append(headline_text)
            
            # Create headlines.txt file
            with open('headlines.txt', 'w') as file:
                for headline in news_headlines:
                    file.write(headline + "\n")
            
            logging.info("Headlines fetched successfully!")
            return news_headlines
        else:
            logging.error(f"Failed to fetch data. Status code: {response.status_code}")
            return ["Unable to fetch headlines at this time."]
    except Exception as e:
        logging.error(f"Failed to scrape headlines: {e}")
        return ["Unable to fetch headlines at this time."]

def send_daily_news():
    with app.app_context():
        emails = Email.query.all()
        headlines = scrape_headlines('https://www.bbc.com/news')
        for email in emails:
            send_email(email.email, headlines)

# Schedule the job to run every minute for testing
scheduler.add_job(func=send_daily_news, trigger="interval", minutes=1)

# Commented out daily schedule
# scheduler.add_job(func=send_daily_news, trigger="cron", hour=8, minute=0)

scheduler.start()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']

        existing_email = Email.query.filter_by(email=email).first()
        if existing_email:
            return 'Email already subscribed!'

        new_email = Email(email=email)
        db.session.add(new_email)
        db.session.commit()
        return 'Thanks for subscribing!'

    return render_template('index.html')

@app.route('/test_email')
def test_email():
    test_email = request.args.get('email', 'yourmail@gmail.com')
    headlines = scrape_headlines('https://www.bbc.com/news')
    send_email(test_email, headlines)
    return f"Test email sent to {test_email}!"

if __name__ == '__main__':
    app.run(debug=True)