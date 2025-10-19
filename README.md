# 🌤️ WeatherWake

**WeatherWake** is a smart alarm clock built with **Python** and **Tkinter**, designed to help you start your day with real-time weather awareness.  
When the alarm goes off, it plays a sound that matches the current weather — rain, sun, clouds, or default — so you know what to expect before you even open your eyes.

---

## 🚀 Features
- ⏰ Custom alarm set by user (HH:MM:SS format)
- 🌎 Automatic location detection via IP
- ☁️ Real-time weather fetched from **OpenWeatherMap API**
- 🎵 Weather-based alarm sounds (e.g., rainy, sunny, cloudy)
- 🔁 Updates weather automatically if conditions change before alarm
- 🖥️ Simple and responsive **Tkinter GUI**
- 🧩 Threaded alarm handling — keeps the UI responsive
- ❌ Manual stop and quit buttons to control the app

---

## 🧱 Project Structure
WeatherWake/
│
├── main.py # Main Python application
├── .env # Contains your secret API key (not uploaded to GitHub)
├── requirements.txt # Project dependencies
├── README.md # This file
└── sounds/ # Folder containing your MP3 alarm files
├── Rainy_alarm_1min.mp3
├── Sunny_alarm_1min.mp3
├── Cloudy_alarm_1min.mp3
└── default_Alarm.mp3


---

## 🔐 Environment Variables
This project uses an `.env` file to store your **OpenWeatherMap API key** securely.

Create a file named `.env` in your project root and add:

API_KEY=your_openweathermap_api_key_here



> ⚠️ Make sure to add `.env` to your `.gitignore` before uploading to GitHub, so your API key stays private.

---

## 🧰 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/WeatherWake.git
cd WeatherWake

2️⃣ Create and activate a virtual environment

python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows

3️⃣ Install dependencies

pip install -r requirements.txt


4️⃣ Add your API key
Create a .env file as shown above.

5️⃣ Run the app

python main.py


⚙️ Requirements
Dependencies are listed in requirements.txt. Example:

tk
pygame
requests
python-dotenv


🧭 How It Works
The app detects your city using your IP address.
It fetches current weather data from the OpenWeatherMap API.
Depending on the weather (Rain, Clear, Clouds, etc.), it assigns a corresponding MP3 alarm sound.
The app continually checks for time and weather updates before the alarm triggers.
When the alarm time matches the system time, your weather-based sound plays.

🧩 Contributing
Contributions are welcome!

If you’d like to enhance the project (new features, better sounds, or design improvements):
Fork the repo
Create a new branch (feature-name)
Commit your changes
Open a Pull Request

🪪 License
This project is open source and free for personal or educational use.
You may modify, distribute, or build upon this project freely with proper credit.

💡 Future Improvements
Add volume control and snooze functionality
Support for multiple alarms
Display weather forecast (not just current condition)
Option to choose custom alarm sounds


🧑‍💻 Author
Jacob Clark
Built with Python, caffeine, and curiosity ☕🐍
