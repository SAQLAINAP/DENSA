# 📰 Densa-App - Your AI-Powered News Butler 🚀  

**Tired of missing out on the latest news?** Let Densa-App do the work! This Flask-powered app scrapes news from **BBC News** and delivers curated updates straight to your inbox. 💌

---

## ⚡ Quick Start (Docker - The Easy Way!)
### 🛠️ 1. Pull the pre-built Docker image
```bash
docker pull saqlainap/densa-app
```

### 🚀 2. Run the container
```bash
docker run -d -p 5000:5000 --env-file .env --name densa saqlainap/densa-app
```

🎉 **Boom!** Open your browser and head to **`http://127.0.0.1:5000/`** to subscribe!

---

## 🔧 Want More Control? Install Manually!
### 1️⃣ Clone the repo
```bash
git clone https://github.com/SAQLAINAP/Densa-App.git
cd Densa-App
```

### 2️⃣ Set up your environment
```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Add your email credentials
Create a `.env` file and add:
```ini
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_password
```

### 4️⃣ Run the app
```bash
flask run
```

🔹 Now visit **`http://127.0.0.1:5000/`** and subscribe to your daily news dose! 🚀

---

## 🎯 Features That Make Densa-App Awesome
✅ **Scrapes & delivers the latest BBC News headlines automatically** 📢  
✅ **Sends emails to subscribers daily using APScheduler** 📩  
✅ **Fully Dockerized for quick & hassle-free deployment** 🐳  
✅ **Lightweight & efficient - runs smoothly on any machine** ⚡  
✅ **No spam, no ads, just pure news goodness** 📰  

---

## 📂 What’s Inside?
```
Densa-App/
│
├── app.py                # Main news scraping & email logic
├── models.py             # Database handling for subscribers
├── templates/            # HTML files for the web interface
├── static/               # CSS & JS files for styling
├── .env                  # Your email credentials (not shared!)
├── Dockerfile            # Container setup
├── requirements.txt      # List of dependencies
└── README.md             # You're reading it!
```

---

## 🌎 Why Use Docker?
💨 **No setup headaches** – Just pull & run!  
🔄 **Same environment everywhere** – No "works on my machine" problems.  
📦 **Perfect for deployment** – Runs on servers, Raspberry Pi, or even your toaster (okay, maybe not your toaster).  

---

## 🤝 Contribute & Be Awesome!
🚀 Got cool ideas? Found a bug? Want to add new features? **We’d love your help!**
1. Fork the repo 🍴
2. Create a branch 🔀
3. Push your changes 🚀
4. Open a Pull Request 🎉

Together, let’s make news smarter! 💡

---

## 📬 Need Help? Let’s Chat!
📧 **Email:** saprophyte.eng@gmail.com  
🐙 **GitHub Repo:** [Densa-App](https://github.com/SAQLAINAP/Densa-App)  
📌 **Docker Hub:** [saqlainap/densa-app](https://hub.docker.com/r/saqlainap/densa-app)  

---

🎤 **Let Densa-App do the reading while you do the living!** 🚀
