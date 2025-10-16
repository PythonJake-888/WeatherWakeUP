# 🌤️ WeatherWake — Weather-Based Python Alarm Clock

WeatherWake is a Python-based alarm clock app that uses **real-time weather data** to customize your wake-up sound.  
It features a simple **Tkinter GUI**, auto-detects your **current city**, and adjusts the alarm tone based on the **current weather conditions** (e.g., sunny, cloudy, rainy).

---

## 🚀 Features

- 🕒 Set alarms easily with a user-friendly GUI  
- 🔊 Plays weather-specific sounds (e.g., rain, sun, clouds, etc.)  
- ☁️ Automatically detects your city using IP geolocation  
- 🌦️ Fetches real-time weather from OpenWeatherMap  
- 🔁 Updates weather before alarm time so it stays accurate  
- ⏹️ Stop or quit the alarm anytime  
- 💻 Cross-platform (Windows, macOS, Linux)

---

## 🧰 Requirements

Make sure you have Python 3.8+ installed, then install the required libraries:

```bash
pip install requests pygame
```

> `tkinter` comes preinstalled with most Python distributions.

---

## 🔑 Setup

1. Clone or download this repository.  
2. Open the script in your favorite Python IDE or terminal.  
3. Replace the example OpenWeatherMap API key in the code:

```python
API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
```

4. Run the script:

```bash
python weatherwake.py
```

---

## 🖥️ How It Works

1. On launch, the app checks your **current location and weather**.
2. Enter a time in the `HH:MM:SS` format.
3. Click **Set Alarm** — the app starts monitoring the clock.
4. When the time matches, the app:
   - Refreshes the current weather
   - Plays a weather-matched alarm sound
   - Displays a message box alert
5. You can click **Stop Alarm** or **Quit App** anytime.

---

## 🔔 Weather-to-Sound Mapping

| Weather | Sound File |
|----------|-------------|
| ☀️ Clear | `Sunny_alarm_1min.mp3` |
| 🌧️ Rain | `Rainy_alarm_1min.mp3` |
| ☁️ Clouds | `Cloudy_alarm_1min.mp3` |
| ❓ Other | `default_Alarm.mp3` |

> You can replace these `.mp3` files with your own — just keep the same filenames or adjust them in the `choose_sound()` function.

---

## 🧩 Code Overview

Main components:
- `get_location()` → Detects your city via IP geolocation.  
- `get_weather(city)` → Fetches live weather from OpenWeatherMap.  
- `choose_sound(weather)` → Picks an alarm sound for the weather.  
- `set_alarm()` → Runs a timer thread that triggers the alarm at the right time.  
- `start_alarm()` and `stop_alarm()` → Button callbacks for the GUI.  

---

## 🛠️ Future Improvements

- Add live weather toggle (“Recheck weather before alarm rings”)  
- Custom sound uploads  
- Multi-alarm scheduling  
- Dark mode GUI  
- Desktop notifications

---

## 📜 License

This project is open-source and free to use for personal projects.  
If you share or modify, please give credit to the original author.

---

## 👤 Author

**Jacob Clark**  
💡 Created with Python, caffeine, and a bit of weather magic ☕🌤️  
