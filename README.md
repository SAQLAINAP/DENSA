# News App

This is a Flask-based web application that sends daily news headlines via email to subscribed users. The application scrapes news headlines from the BBC News website and sends them to the subscribers' email addresses.

## Features
- **User subscription to daily news emails**
- **Scraping news headlines from BBC News**
- **Sending daily news emails with the latest headlines**
- **Scheduling daily email sending using APScheduler**

## Prerequisites
To run this application, you need:
- Python 3.x
- Flask
- Flask-Mail
- Flask-SQLAlchemy
- APScheduler
- Requests
- BeautifulSoup4
- python-dotenv

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the `news_app` directory and add your email configuration:**
   ```
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_password
   ```

5. **Initialize the database:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

## Usage

1. **Run the Flask application:**
   ```bash
   flask run
   ```

2. **Open your web browser and go to** `http://127.0.0.1:5000/`.

3. **Subscribe to the daily news emails by entering your email address on the homepage.**

The application will scrape the latest news headlines from BBC News and send them to the subscribed email addresses every day.

## File Structure

```
news_app/
│
├── app.py                # Main application file
├── models.py             # Database models
├── templates/            # HTML templates for rendering views
│   └── index.html        # Homepage template
├── static/               # Static files (CSS, JS, images)
├── .env                  # Environment variables for configuration
└── requirements.txt       # List of dependencies
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Flask
- Flask-Mail
- Flask-SQLAlchemy
- APScheduler
- Requests
- BeautifulSoup4

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or suggestions, please contact [saprophyte.eng@gmail.com]
