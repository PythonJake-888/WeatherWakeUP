# main.py - WeatherWake Alarm Clock

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

print("WeatherWake app starting...")
print(f"Loaded API Key: {'FOUND' if API_KEY else 'MISSING'}")


#Weather Wake Python Alarm clock

#GUI Libraries
import tkinter as tk
from tkinter import messagebox


#Import Libraries for Alarm Clock and Audio

import time
import datetime
import threading
import pygame

#imports for API

import requests




stop_alarm_flag = False

#---------------WEATHER FUNCTIONS ---------------



def get_location():
    """Get user city using IP geolocation."""

    try:
        response = requests.get("http://ip-api.com/json/").json()
        return response.get("city", "Unknown")
    except:
        return "Unknown"

def get_weather(city):
    """Fetch weather for given city."""

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        data = requests.get(url).json()
        if "weather" in data:
            return data["weather"][0]["main"]
    except:
        pass
    return "Unknown"


def choose_sound(weather):
    """Pick alarm sound file based on weather condition"""

    if weather == "Rain":
        return "Rainy_alarm_1min.mp3"
    elif weather == "Clear":
        return "Sunny_alarm_1min.mp3"
    elif weather == "Clouds":
        return "Cloudy_alarm_1min.mp3"
    else:
        return "default_Alarm.mp3"

def get_weather_icon(weather):
    """Get weather icon based on weather condition"""
    if weather == "Rain":
        return "\U0001F327"
    elif weather == "Clear":
        return "\U0001F31E"
    elif weather == "Clouds":
        return "\u2601"
    else:
        return "\U00002753"


#Main Application Window

def set_alarm(alarm_time, sound_file):
    global stop_alarm_flag

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        clock_label.config(text=f"Current Time: {current_time}")#Update Gui clock
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
    """Start alarm sound."""
    global stop_alarm_flag
    alarm_time = entry.get()

    if alarm_time == "":
         messagebox.showerror("Error", "Please enter a time in HH:MM:SS format.")
         return

    stop_alarm_flag = False

    city = get_location()
    weather = get_weather(city)
    sound_file = choose_sound(weather)
    icon = get_weather_icon(weather)

    weather_label.config(text=f"Weather in {city} : {weather}  {icon}")
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")

    t = threading.Thread(target=set_alarm, args=(alarm_time,sound_file), daemon=True)
    t.start()


def stop_alarm():
    """Stop alarm."""
    global stop_alarm_flag
    stop_alarm_flag = True
    try:
        pygame.mixer.music.stop()
    except:
        pass

    messagebox.showinfo("Alarm Stopped", "Alarm Stopped")

def update_clock():
    """Update the clock."""
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=f"Current Time: {current_time}")
    root.after(1000, update_clock)

def update_weather():
    """ Update weather icon based on weather condition"""

    city = get_location()
    weather = get_weather(city)
    icon = get_weather_icon(weather)
    weather_label.config(text=f"Weather in {city} : {weather}  {icon}")
    root.after(3600000, update_weather)

#GUI setup

root = tk.Tk()
root.title("WeatherWake")
root.geometry("600x400")

# Title GUI
tk.Label(root, text="Enter Alarm Time(HH:MM:SS)").pack(pady=5)

entry = tk.Entry(root, font=("Arial",  14), justify="center")
entry.pack(pady=5)

# Button initialization

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

#Button Layout

tk.Button(btn_frame, text="Set Alarm", width = 12, command = start_alarm).grid(row= 0 , column = 0 , padx=5)
tk.Button(btn_frame, text = "Stop Alarm", width= 12, command= stop_alarm).grid(row=0,column=1,padx=5)
tk.Button(btn_frame, text="Quit", width = 12, command = root.destroy).grid(row=0,column=2,padx=5)

#Clock GUI Layout
clock_label= tk.Label(root, text ="Current Time: --:--:--", font=("Arial", 12))
clock_label.pack(pady=10)

#Weather GUI Layout
weather_label = tk.Label(root, text="Weather: Unknown ", font=("Arial", 14))
weather_label.pack(pady=10)

# Call Update clock. and weather at program launch

update_clock()
update_weather()

root. mainloop()
