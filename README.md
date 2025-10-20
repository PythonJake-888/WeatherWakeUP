# 🌦️ WeatherWake: Smart Weather-Based Alarm Clock

**WeatherWake** is a Python-based alarm clock that integrates live weather data to wake you up with environment-specific sounds — whether it’s raining, sunny, or cloudy!  
The app uses your **IP-based location**, fetches the **current weather**, and plays a **customized alarm sound** that matches the forecast.  

---

## 📁 Project Structure

```
WeatherWake/
│
├── main.py                  # Main application file
├── .env                     # Hidden file storing your API key (not uploaded)
├── .gitignore               # Prevents sensitive and unnecessary files from being committed
├── README.md                # Documentation file
├── requirements.txt         # Python dependencies
└── Sounds/
    ├── Rainy_alarm_1min.mp3
    ├── Sunny_alarm_1min.mp3
    ├── Cloudy_alarm_1min.mp3
    └── default_Alarm.mp3
```

---

## ⚙️ Installation and Setup

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/PythonJake-888/WeatherWakeUP.git
cd WeatherWakeUP
```

### **Step 2: Set Up a Virtual Environment**

It’s best to create a virtual environment for your project.

```bash
python -m venv venv
source venv/bin/activate   # (Mac/Linux)
venv\Scripts\activate      # (Windows)
```

### **Step 3: Install Required Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 4: Set Up Your OpenWeather API Key**

1. Create a free account at [OpenWeatherMap](https://openweathermap.org/api).  
2. Generate your **API key**.  
3. In the project root folder, create a file named `.env` and add your key:

   ```bash
   OPENWEATHER_API_KEY=your_openweather_api_key_here
   ```

### **Step 5: Run the App**

```bash
python main.py
```

---

## 🧩 Requirements

- Python 3.8 or later  
- Internet connection (for weather updates)
- The following Python libraries:
  - `pygame`
  - `requests`
  - `python-dotenv`
  - `tkinter` (included by default with Python)

---

## 💡 How It Works

1. **Weather Detection:** Uses IP geolocation to identify your current city.  
2. **API Integration:** Fetches weather data from OpenWeatherMap.  
3. **Dynamic Alarm Sounds:** Plays weather-specific sounds (rain, sun, or clouds).  
4. **Live Updates:** The app updates weather info hourly in the background.  
5. **Custom Controls:** You can stop the alarm or quit the app at any time.

---

## 🧠 Features

- 🎵 Weather-based alarm tones  
- 🕒 Live clock display  
- 🌤 Hourly weather updates  
- 🧭 Automatic location detection  
- 🧰 Simple and clean Tkinter GUI  
- 🔐 Hidden API key support via `.env`  

---

## 🔒 API Key Security

Your `.env` file contains your private API key.  
Make sure it’s **never uploaded** to GitHub by including `.env` in your `.gitignore` file.

Example `.gitignore`:
```
.env
__pycache__/
*.pyc
*.mp3
```

---

## 🤝 Contributing

Contributions are welcome!  
You can:
- Submit bug reports
- Suggest new features (e.g., voice alarms, snooze mode)
- Improve documentation

To contribute:
1. Fork the repository  
2. Create a new branch  
3. Commit your changes  
4. Open a pull request

---

## 👨‍💻 Author

**Created by:** [Jake Clark (PythonJake-888)](https://github.com/PythonJake-888)  
*WeatherWake — Bringing weather and wake-ups together.* ☀️🌧️🌙

---

## 🪪 License

This project is licensed under the **MIT License**, meaning it’s open-source and free to modify or distribute with attribution.

---
