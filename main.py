"""
WeatherWake Alarm Clock
-----------------------
A Python GUI alarm clock that:
- Displays current time and weather based on the user's location.
- Plays different alarm sounds depending on the weather.
- Updates weather data hourly.
"""

# === Imports ===
import os
import time
import datetime
import threading
import tkinter as tk
from tkinter import messagebox

import pygame
import requests
from dotenv import load_dotenv


# === Load Environment Variables ===
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

print("WeatherWake app starting...")
print(f"Loaded API Key: {'FOUND' if API_KEY else 'MISSING'}")

# === Global Variables ===
stop_alarm_flag = False


# =============================
#        WEATHER FUNCTIONS
# =============================
def get_location():
    """Get the user's city using IP geolocation."""
    try:
        response = requests.get("http://ip-api.com/json/").json()
        return response.get("city", "Unknown")
    except Exception:
        return "Unknown"


def get_weather(city):
    """Fetch weather for the given city using OpenWeatherMap API."""
    if not API_KEY:
        return "Unknown"

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        data = requests.get(url).json()
        if "weather" in data:
            return data["weather"][0]["main"]
    except Exception:
        pass
    return "Unknown"


def choose_sound(weather):
    """Select an alarm sound file based on weather condition (case-insensitive)."""
    print(f"Weather API returned: {weather}")
    if not weather:
        return "Sounds/default_Alarm.mp3"

    weather = weather.lower()

    if "rain" in weather:
        return "Sounds/Rainy_alarm_1min.mp3"
    if "clear" in weather or "sun" in weather:
        return "Sounds/Sunny_alarm_1min.mp3"
    if "cloud" in weather:
        return "Sounds/Cloudy_alarm_1min.mp3"

    return "Sounds/default_Alarm.mp3"


def get_weather_icon(weather):
    """Get a Unicode weather icon based on the condition."""
    weather = weather.lower() if weather else ""
    if "rain" in weather:
        return "\U0001F327"  # 🌧
    if "clear" in weather or "sun" in weather:
        return "\U0001F31E"  # 🌞
    if "cloud" in weather:
        return "\u2601"      # ☁
    return "\U00002753"      # ❓


# =============================
#         ALARM LOGIC
# =============================
def set_alarm(alarm_time, sound_file):
    """Continuously check the current time and trigger the alarm when matched."""
    global stop_alarm_flag

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        clock_label.config(text=f"Current Time: {current_time}")

        if current_time == alarm_time:
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            messagebox.showinfo("Alarm", f"Wake Up!\nWeather sound: {sound_file}")

            while pygame.mixer.music.get_busy():
                if stop_alarm_flag:
                    pygame.mixer.music.stop()
                    break
                time.sleep(1)

        if stop_alarm_flag:
            break
        time.sleep(1)


def start_alarm():
    """Start the alarm sound at the specified time."""
    global stop_alarm_flag
    alarm_time = entry.get().strip()

    if not alarm_time:
        messagebox.showerror("Error", "Please enter a time in HH:MM:SS format.")
        return

    stop_alarm_flag = False
    city = get_location()
    weather = get_weather(city)
    sound_file = choose_sound(weather)
    icon = get_weather_icon(weather)

    weather_label.config(text=f"Weather in {city}: {weather} {icon}")
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")

    thread = threading.Thread(target=set_alarm, args=(alarm_time, sound_file), daemon=True)
    thread.start()


def stop_alarm():
    """Stop the alarm sound."""
    global stop_alarm_flag
    stop_alarm_flag = True
    try:
        pygame.mixer.music.stop()
    except Exception:
        pass
    messagebox.showinfo("Alarm Stopped", "Alarm stopped.")


# =============================
#       LIVE UPDATES
# =============================
def update_clock():
    """Update the displayed clock every second."""
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=f"Current Time: {current_time}")
    root.after(1000, update_clock)


def update_weather():
    """Update the weather every hour."""
    city = get_location()
    weather = get_weather(city)
    icon = get_weather_icon(weather)
    weather_label.config(text=f"Weather in {city}: {weather} {icon}")
    root.after(3600000, update_weather)  # Update every hour


# =============================
#          GUI SETUP
# =============================
root = tk.Tk()
root.title("WeatherWake")
root.geometry("600x400")

# Alarm Entry
tk.Label(root, text="Enter Alarm Time (HH:MM:SS)").pack(pady=5)
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Set Alarm", width=12, command=start_alarm).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Stop Alarm", width=12, command=stop_alarm).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Quit", width=12, command=root.destroy).grid(row=0, column=2, padx=5)

# Labels
clock_label = tk.Label(root, text="Current Time: --:--:--", font=("Arial", 12))
clock_label.pack(pady=10)

weather_label = tk.Label(root, text="Weather: Unknown", font=("Arial", 14))
weather_label.pack(pady=10)

# Launch updates
update_clock()
update_weather()

root.mainloop()
