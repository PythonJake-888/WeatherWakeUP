# WeatherWake Alarm Clock

A Python-based weather-aware alarm clock with a graphical interface built using Tkinter.
The app automatically detects your location, fetches current weather from OpenWeatherMap,
and plays a unique alarm sound based on the weather conditions.

## Features
- Real-time weather detection
- Custom alarm sounds (Rain, Sun, Clouds, Default)
- GUI with live clock and weather display
- Start/Stop alarm buttons
- Secure API key handling using .env files

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the same folder as `main.py`:
   ```bash
   OPENWEATHER_API_KEY=your_api_key_here
   ```

3. Run the app:
   ```bash
   python main.py
   ```

4. (Optional) Add alarm sounds to the `sounds/` folder.

## Repository Structure
```
WeatherWake/
├── main.py
├── .env (hidden, not uploaded)
├── .env.example
├── WeatherWake_README.md
├── requirements.txt
├── .gitignore
└── sounds/
```

## License
MIT License (Feel free to modify and share!)
