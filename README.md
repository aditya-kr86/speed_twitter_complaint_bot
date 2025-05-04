Here's a professional, casual, and opinionated `README.md` for your project **Internet Speed Tracker and Complainer Bot** using Selenium and Twitter (X):

---

# 🛰️ Internet Speed Tracker and Complainer Bot

This Python bot checks your internet speed using [Speedtest.net](https://www.speedtest.net/) and tweets a complaint at your internet provider if your speed is below the promised threshold. It automates the frustration—so you don't have to.

## 🚀 Features

* 📶 Automatically visits **speedtest.net** and measures your **download/upload speeds**
* 🧠 Compares the result with your **promised plan**
* 🐦 Logs into **X (Twitter)** and tweets a complaint if the speed is unsatisfactory
* ✅ Runs in Chrome with maximized window and detachment option enabled
* 😎 Fully hands-off once configured

---

## 🧠 How It Works

1. Launches Chrome using Selenium
2. Measures internet speed from Speedtest.net
3. Logs into your X (Twitter) account
4. Tweets a message if the actual speed is below the expected thresholds

---

## 🛠️ Requirements

* Python 3.7+
* Google Chrome installed
* ChromeDriver matching your Chrome version
* X (Twitter) account credentials (hardcoded for now)
* Libraries:

  * `selenium`
  * `time` (built-in)

Install dependencies:

```bash
pip install selenium
```

Make sure ChromeDriver is in your PATH or specify the path explicitly in the script.

---

## ⚙️ Configuration

Set your promised internet speed and X (Twitter) credentials in the script:

```python
PROMISED_DOWN = 10  # Mbps
PROMISED_UP = 5     # Mbps
X_USERNAME = 'your_username'
X_PASSWORD = 'your_password'
```

(Yes, credentials are hardcoded. No, you shouldn’t do that in production—use environment variables or a config file instead.)

---

## 📄 Usage

Run the script:

```bash
python bot.py
```

It will:

* Open Speedtest → Measure speeds
* Visit X → Log in
* Tweet a complaint like:

> "Hey internet provider, Why is my internet speed 5.2down/0.8up when I pay for 10down/5up?"

---

## 📸 Screenshot

*(Optional — Add a screenshot of the tweet or console output)*

---

## 🧠 Future Improvements

* [ ] Store credentials securely (e.g., `.env` file)
* [ ] Add logging
* [ ] Support for other social media/email
* [ ] GUI with Tkinter or Web UI with Flask

---

## ⚠️ Disclaimer

This is a fun project meant for educational purposes only. Don’t actually spam your provider unless your speed is genuinely horrible. 😅

---

## 👨‍💻 Author

**Aditya Kumar**
Student | Python Developer | Automation Enthusiast
[adityakr.me](https://adityakr.me) | [GitHub](https://github.com/aditya-kr86) | [LinkedIn](https://linkedin.com/in/aditya-kr86))

