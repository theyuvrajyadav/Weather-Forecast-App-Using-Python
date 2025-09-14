# Weather Forecast App

A simple Python GUI application that displays current weather information for any city using the OpenWeatherMap API.

## Features

- Clean and user-friendly Tkinter interface
- Real-time weather data from OpenWeatherMap API
- Displays temperature, feels like temperature, weather description, humidity, and wind speed
- Error handling for invalid city names or API issues
- Visual feedback based on temperature (color changes)
- Status bar with operation information

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)
- Requests library

## Installation

1. Clone or download this repository
2. Install the required packages:

```
pip install requests
```

## Getting an API Key

To use this application, you need to obtain a free API key from OpenWeatherMap:

1. Go to [OpenWeatherMap](https://openweathermap.org/) and create a free account
2. After signing up, go to your account page and navigate to the "API Keys" section
3. Generate a new API key (it may take a few hours to activate)
4. Copy your API key

## Setup

1. Open `weather_app.py` in a text editor
2. Find the line `self.api_key = ""` (around line 18)
3. Replace the empty string with your OpenWeatherMap API key: `self.api_key = "your_api_key_here"`
4. Save the file

## Usage

1. Run the application:

```
python weather_app.py
```

2. Enter a city name in the input field
3. Click the "Search" button or press Enter
4. The weather information will be displayed in the main window

## Features

- **Search**: Enter a city name and click Search or press Enter
- **Clear**: Reset the input field and weather display
- **Error Handling**: The app will display appropriate error messages if the city is not found or if there are API connection issues
- **Visual Feedback**: The background color of the weather information changes based on temperature (blue for cold, orange for hot)

## License

This project is open source and available under the MIT License.