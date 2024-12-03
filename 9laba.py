import tkinter as tk
import requests

API_KEY = '2a8021af2652d529e9f4cdfbea734206' 

def get_weather():
    city = "Ulyanovsk"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            weather_label.config(text=f"Погода в Ульяновске: {temperature}°C, {weather_description}")
        else:
            weather_label.config(text="Ошибка запроса погоды!")
    except Exception as e:
        weather_label.config(text="Ошибка подключения!")

# Создание метки для отображения погоды
weather_label = tk.Label(root, text="", justify=tk.LEFT, fg="blue")
weather_label.pack(pady=10)

# Кнопка для обновления погоды
weather_button = tk.Button(root, text="Получить погоду", command=get_weather)
weather_button.pack(pady=10)
