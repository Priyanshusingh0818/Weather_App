import tkinter as tk
from tkinter import ttk, messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")


        self.city_var = tk.StringVar()
        self.unit_var = tk.StringVar(value="metric")


        self.label_city = ttk.Label(root, text="Enter city:")
        self.entry_city = ttk.Entry(root, textvariable=self.city_var, font=('Arial', 14))
        self.label_unit = ttk.Label(root, text="Select unit:")
        self.unit_options = ["metric"]
        self.unit_menu = ttk.Combobox(root, textvariable=self.unit_var, values=self.unit_options, font=('Arial', 14))
        self.unit_menu.set("metric")
        self.get_weather_button = ttk.Button(root, text="Get Weather", command=self.get_weather)
        self.result_label = ttk.Label(root, text="", font=('Arial', 16))


        self.label_city.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.entry_city.grid(row=0, column=1, pady=10, padx=10)
        self.label_unit.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.unit_menu.grid(row=1, column=1, pady=10, padx=10)
        self.get_weather_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def get_weather(self):
        api_key = '95f052e0f9a6394d997fe6f408999640'
        city = self.city_var.get()
        unit = self.unit_var.get()

        if not city:
            messagebox.showinfo("Error", "Please enter a city.")
            return

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={unit}'

        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()
            description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            result_text = f"Weather: {description}\nTemperature: {temperature}°C"
            self.result_label.config(text=result_text)
        except requests.exceptions.RequestException as e:
            self.result_label.config(text="Error fetching weather data")
            messagebox.showinfo("Error", f"Error fetching weather data: {e}")
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
