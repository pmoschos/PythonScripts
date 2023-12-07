import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import ttkbootstrap
from configs import API_KEY

def get_weather(city):
    """
    Fetches the weather information for a given city.

    Parameters:
    city (str): The name of the city for which the weather is requested.

    Returns:
    tuple: A tuple containing the icon URL, temperature, weather description, city name, and country code.
    None: If the city is not found or an error occurs.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    response = requests.get(url)

    if response.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    weather_data = response.json()
    icon_id = weather_data['weather'][0]['icon']
    temperature_celsius = weather_data['main']['temp'] - 273.15
    weather_description = weather_data['weather'][0]['description']
    city_name = weather_data['name']
    country_code = weather_data['sys']['country']

    icon_url = f'https://openweathermap.org/img/wn/{icon_id}@2x.png'

    return (icon_url, temperature_celsius, weather_description, city_name, country_code)

def search_weather():
    """
    Searches for the weather of the city entered in the city_entry widget,
    and updates the GUI components with the retrieved weather information.
    """
    city = city_entry.get()
    weather_info = get_weather(city)
    if weather_info is None:
        return

    icon_url, temperature, description, city, country = weather_info
    location_label.configure(text=f"{city}, {country}")
    
    weather_icon_image = Image.open(requests.get(icon_url, stream=True).raw)
    weather_icon = ImageTk.PhotoImage(weather_icon_image)
    icon_label.configure(image=weather_icon)
    icon_label.image = weather_icon

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")

def on_entry_click(event):
    """Clear the entry field when it is clicked."""
    if city_entry.get() == 'Enter a city name':
        city_entry.delete(0, "end")  # delete all the text in the entry
        city_entry.insert(0, '')  # Insert blank for user input

def on_focusout(event):
    """Add hint text when the entry field loses focus and is empty."""
    if city_entry.get() == '':
        city_entry.insert(0, 'Enter a city name')

# Setting up the main window using ttkbootstrap
root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400x400")

city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.insert(0, 'Enter a city name')  # Default text
city_entry.bind('<FocusIn>', on_entry_click)  # Bind event to function call
city_entry.bind('<FocusOut>', on_focusout)  # Bind event to function call
city_entry.pack(pady=10)

search_button = ttkbootstrap.Button(root, text="Search", command=search_weather, bootstyle="warning")
search_button.pack(pady=10)

location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

icon_label = tk.Label(root)
icon_label.pack()

temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()
