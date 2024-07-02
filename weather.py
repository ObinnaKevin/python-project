import requests
API_KEY = "a709300cc6e943b8fc2978e1e287bb21"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
         "q" : city,
         "appid" : API_KEY,
         "units" : "metric"
}
    response = requests.get(BASE_URL, params = params)
    

    if response.status_code == 200:
       data = response.json()
       weather = {
           "name" : data["name"],
           "temperature" : data["main"]["temp"], 
           "description" : data["weather"][0]["description"],
           "humidity" : data["main"]["humidity"],
           "wind_speed" : data["wind"]["speed"]
       }
       return weather
    else:
        print("error weather for city not found")
    return 

def display_weather(weather):
    if weather:
        print(f"city:{weather["name"]}")
        print(f"temperature:{weather["temperature"]}")
        print(f"description:{weather["description"]}")
        print(f"humidity: {weather["humidity"]}")
        print(f"wind_speed: {weather ["wind_speed"]}")
    else:
        print("could not retrieve weathwr report")
def run_all():
    city = input("enter your city:")
    weather = get_weather(city)
    display_weather(weather)
run_all()





# import tkinter as tk
# import requests

# API_KEY = "a709300cc6e943b8fc2978e1e287bb21"
# BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# def get_weather(city):
#     params = {
#         "q": city,
#         "appid": API_KEY,
#         "units": "metric"
#     }
#     response = requests.get(BASE_URL, params=params)
    
#     if response.status_code == 200:
#         data = response.json()
#         weather = {
#             "name": data["name"],
#             "temperature": data["main"]["temp"], 
#             "description": data["weather"][0]["description"],
#             "humidity": data["main"]["humidity"],
#             "wind_speed": data["wind"]["speed"]
#         }
#         return weather
#     else:
#         return None

# def display_weather(weather):
#     if weather:
#         result_label.config(text=f"City: {weather['name']}\n"
#                                 f"Temperature: {weather['temperature']} °C\n"
#                                 f"Description: {weather['description']}\n"
#                                 f"Humidity: {weather['humidity']}%\n"
#                                 f"Wind Speed: {weather['wind_speed']} m/s")
#     else:
#         result_label.config(text="Weather information not found.")

# def get_weather_and_display():
#     city = city_entry.get()
#     weather = get_weather(city)
#     display_weather(weather)

# # Create the main application window
# root = tk.Tk()
# root.title("Weather App")

# # Create GUI elements
# label = tk.Label(root, text="Enter city:")
# label.pack(pady=10)

# city_entry = tk.Entry(root, width=30)
# city_entry.pack()

# get_weather_button = tk.Button(root, text="Get Weather", command=get_weather_and_display)
# get_weather_button.pack(pady=10)

# result_label = tk.Label(root, text="", wraplength=400)
# result_label.pack(pady=20)

# # Start the main tkinter event loop
# root.mainloop()



    
