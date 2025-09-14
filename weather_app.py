import tkinter as tk
from tkinter import messagebox, ttk
import requests
import json
from datetime import datetime

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")
        self.root.geometry("450x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#E8F5FE")
        
        # API Key for OpenWeatherMap
        self.api_key = "" # You need to add your API key here
        
        # Create app title
        self.app_title = tk.Label(root, text="Weather Forecast App", font=("Helvetica", 18, "bold"), 
                                bg="#E8F5FE", fg="#2C3E50")
        self.app_title.pack(pady=(20, 10))
        
        # Create frames with rounded corners effect
        self.input_frame = tk.Frame(root, bg="#FFFFFF", bd=2, relief=tk.GROOVE)
        self.input_frame.pack(pady=15, padx=20, fill="x")
        
        self.result_frame = tk.Frame(root, bg="#FFFFFF", bd=2, relief=tk.GROOVE)
        self.result_frame.pack(pady=15, padx=20, fill="both", expand=True)
        
        # Create input elements
        self.city_label = tk.Label(self.input_frame, text="Enter City Name:", font=("Helvetica", 12), 
                                 bg="#FFFFFF", fg="#2C3E50")
        self.city_label.grid(row=0, column=0, padx=10, pady=15)
        
        self.city_entry = tk.Entry(self.input_frame, font=("Helvetica", 12), width=20, bd=2, relief=tk.GROOVE)
        self.city_entry.grid(row=0, column=1, padx=10, pady=15)
        self.city_entry.focus()
        
        # Bind Enter key to get_weather function
        self.city_entry.bind("<Return>", lambda event: self.get_weather())
        
        # Button frame for better organization
        self.button_frame = tk.Frame(self.input_frame, bg="#FFFFFF")
        self.button_frame.grid(row=0, column=2, padx=10, pady=15)
        
        # Search button with hover effect
        self.search_button = tk.Button(self.button_frame, text="Search", font=("Helvetica", 10, "bold"), 
                                     bg="#3498DB", fg="white", width=8, cursor="hand2",
                                     activebackground="#2980B9", command=self.get_weather)
        self.search_button.pack(side=tk.LEFT, padx=2)
        
        # Clear button
        self.clear_button = tk.Button(self.button_frame, text="Clear", font=("Helvetica", 10, "bold"), 
                                    bg="#E74C3C", fg="white", width=8, cursor="hand2",
                                    activebackground="#C0392B", command=self.clear_input)
        self.clear_button.pack(side=tk.LEFT, padx=2)
        
        # Create result elements
        self.result_title = tk.Label(self.result_frame, text="Weather Information", 
                                   font=("Helvetica", 14, "bold"), bg="#FFFFFF", fg="#2C3E50")
        self.result_title.pack(pady=10)
        
        # Separator
        ttk.Separator(self.result_frame, orient='horizontal').pack(fill='x', padx=20)
        
        # Weather info display with better styling
        self.weather_info = tk.Label(self.result_frame, text="Enter a city name and click Search", 
                                   font=("Helvetica", 12), bg="#FFFFFF", fg="#7F8C8D",
                                   width=40, height=12, anchor="n", justify=tk.LEFT)
        self.weather_info.pack(pady=15, padx=20)
        
        # Status bar
        self.status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W, 
                                 font=("Helvetica", 8), bg="#F0F0F0", fg="#7F8C8D")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def clear_input(self):
        """Clear the input field and reset the weather display"""
        self.city_entry.delete(0, tk.END)
        self.weather_info.config(text="Enter a city name and click Search", fg="#7F8C8D")
        self.status_bar.config(text="Ready")
        self.city_entry.focus()
    
    def get_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showerror("Error", "Please enter a city name!")
            return
        
        self.weather_info.config(text="Fetching weather data...", fg="#3498DB")
        self.status_bar.config(text=f"Searching for weather in {city}...")
        self.root.update()
        
        try:
            # Make API request to OpenWeatherMap
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            
            # Check if the request was successful
            if response.status_code == 200:
                weather_data = response.json()
                self.display_weather(weather_data)
                self.status_bar.config(text=f"Weather data retrieved successfully at {datetime.now().strftime('%H:%M:%S')}")
            else:
                if response.status_code == 404:
                    messagebox.showerror("Error", f"City '{city}' not found!")
                    self.status_bar.config(text=f"Error: City '{city}' not found")
                else:
                    messagebox.showerror("Error", f"Error fetching weather data: {response.status_code}")
                    self.status_bar.config(text=f"Error: Failed to fetch weather data (Code: {response.status_code})")
                self.weather_info.config(text="No weather data to display", fg="#E74C3C")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_bar.config(text="Error: Failed to connect to weather service")
            self.weather_info.config(text="No weather data to display", fg="#E74C3C")
    
    def display_weather(self, data):
        # Extract weather information
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        
        # Get weather icon code and determine if it's day or night
        weather_icon = data["weather"][0]["icon"]
        
        # Format the weather information with better styling
        weather_info = f"City: {city_name}, {country}\n\n"
        weather_info += f"Temperature: {temp:.1f}°C\n"
        weather_info += f"Feels Like: {feels_like:.1f}°C\n"
        weather_info += f"Weather: {description.title()}\n"
        weather_info += f"Humidity: {humidity}%\n"
        weather_info += f"Wind Speed: {wind_speed:.1f} m/s\n\n"
        weather_info += f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        # Update the weather information label with appropriate color based on temperature
        self.weather_info.config(text=weather_info, fg="#2C3E50")
        
        # Change background color based on temperature for visual feedback
        if temp < 10:
            self.weather_info.config(bg="#E8F8FF")  # Cold - light blue
        elif temp > 30:
            self.weather_info.config(bg="#FFF0E8")  # Hot - light orange/red
        else:
            self.weather_info.config(bg="#FFFFFF")  # Normal - white

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()