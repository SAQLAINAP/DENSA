# News App

This is a Flask-based web application that sends daily news headlines via email to subscribed users. The application scrapes news headlines from the BBC News website and sends them to the subscribers' email addresses.

## Features
- **User subscription to daily news emails**
- **Scraping news headlines from BBC News**
- **Sending daily news emails with the latest headlines**
- **Scheduling daily email sending using APScheduler**
- **Supports both manual and Docker-based execution**

---

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
- Docker (for containerized execution)

---

## Installation & Setup (Manual Execution)

### 1. Clone the repository:
```bash
git clone <repository-url>
cd news_app
```

### 2. Create a virtual environment and activate it:
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install the required packages:
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the `news_app` directory and add your email configuration:
```ini
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_password
```

### 5. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

### 6. Run the Flask application:
```bash
flask run
```

### 7. Open your web browser and go to:
```
http://127.0.0.1:5000/
```

### 8. Subscribe to the daily news emails by entering your email address on the homepage.

The application will scrape the latest news headlines from BBC News and send them to the subscribed email addresses every day.

---

## Running with Docker (Containerized Execution)

### 1. Clone the repository:
```bash
git clone <repository-url>
cd news_app
```

### 2. Create an `.env` file with email configuration:
```ini
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_password
```

### 3. Build the Docker image:
```bash
docker build -t news-app .
```

### 4. Run the application in a Docker container:
```bash
docker run -d -p 5000:5000 --env-file .env --name news_app_container news-app
```

### 5. Open your web browser and go to:
```
http://127.0.0.1:5000/
```

### 6. Subscribe to receive daily news emails.

---

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
├── Dockerfile            # Dockerfile for containerized execution
├── requirements.txt       # List of dependencies
└── README.md             # Documentation
```

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgements
- Flask
- Flask-Mail
- Flask-SQLAlchemy
- APScheduler
- Requests
- BeautifulSoup4
- Docker

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## Contact
For any questions or suggestions, please contact [saprophyte.eng@gmail.com]
