# DENSA
Daily Email News Subscription App is a Python-based web application built with Flask. It allows users to subscribe with their email to receive daily news headlines via email. The app scrapes news from the BBC News website . The app includes email validation, SQLite database storing subscriptions, and features a clean landing page for subscribing.
---

### **Project Title:** Daily News Email Subscription App

**Description:**

This project is a Python-based web application built with Flask. It allows users to subscribe with their email to receive daily news headlines via email. The app scrapes news from the BBC News website and uses a background scheduler to send the headlines to subscribers at scheduled intervals (daily or for testing purposes, every minute). The app includes email validation, SQLite database for storing subscriptions, and features a clean landing page for subscribing.

**Key Features:**
- Flask-based web app for email subscription
- Background scheduler to send daily news via email
- Web scraping of BBC News headlines using `BeautifulSoup`
- Flask-Mail integration for sending emails
- SQLite database to manage email subscriptions
- Simple and responsive UI for users to subscribe

---

### **README.md**:

# Daily News Email Subscription App

This project is a simple news subscription web application built using Flask. Users can subscribe with their email to receive daily news headlines from the BBC directly in their inbox.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Email Subscription:** Allows users to subscribe with their email to receive daily news.
- **News Scraping:** Scrapes news headlines from [BBC News](https://www.bbc.com/news) using BeautifulSoup.
- **Automated Emails:** Emails are automatically sent to all subscribers at scheduled intervals using Flask-Mail and APScheduler.
- **Database Integration:** Email addresses are stored in an SQLite database.
- **Responsive Web Interface:** A minimalistic web form for subscribing to the mailing list.

## Technologies Used
- **Python 3.x**
- **Flask**
- **Flask-Mail**
- **Flask-SQLAlchemy**
- **BeautifulSoup (for web scraping)**
- **APScheduler (for scheduling tasks)**
- **SQLite** (for database management)

## Installation
To run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/news-subscription-app.git
   cd news-subscription-app
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables in a `.env` file (see [Environment Variables](#environment-variables) section).

5. Initialize the SQLite database:
   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

6. Run the app:
   ```bash
   flask run
   ```

## Usage

- **Landing Page:** Open `http://127.0.0.1:5000` in your browser and enter your email to subscribe.
- **Test Email:** Use `http://127.0.0.1:5000/test_email` to send a test email with current news headlines.
- **Automatic Emailing:** The app is configured to send daily news emails to all subscribers. You can modify the schedule by adjusting the `APScheduler` settings in the code.

## Environment Variables
Create a `.env` file in the root of your project and add the following variables:

```bash
EMAIL_USER=<your-email@example.com>
EMAIL_PASS=<your-email-password>
```

These are used for sending emails via SMTP. Ensure that SMTP is properly configured for your email provider (e.g., Gmail).

## Contributing
If you'd like to contribute to this project, feel free to submit a pull request with your changes.

1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Added a new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a Pull Request on GitHub

## License
This project is licensed under the MIT License. See the LICENSE file for more information.


---

### **`requirements.txt`**:

Add this file to your repository to list the dependencies required for your application:
```
Flask==2.0.1
Flask-Mail==0.9.1
Flask-SQLAlchemy==2.5.1
APScheduler==3.6.3
beautifulsoup4==4.9.3
requests==2.26.0
python-dotenv==0.19.0
```

---

### **`.gitignore`**:

This will help avoid committing unnecessary files like your virtual environment, IDE settings, and cache files.

```bash
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# Virtual environment folder
venv/

# Environment variables file
.env

# macOS files
.DS_Store

# Logs
*.log
```

---

### **LICENSE:**

```
MIT License

Copyright (c) 2024 Saqlain Ahmed P

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

...
```
