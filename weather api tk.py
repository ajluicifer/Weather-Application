# importing required library
import tkinter as tk
import os
import requests
from datetime import datetime

# Getting API ID as system variable
apiid = os.environ["api"]

# Defining function for binding with Entry widgth
def weather(box):

    city_name = textfield.get()    # Getting Value from Textfield widgth
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name  + "&appid=" + apiid

    api_link = requests.get(api)
    api_data = api_link.json()   #Receive Data using API link in JSON format

    date_time = datetime.now().strftime("%d-%m-%y || %H:%M:%S")

    country_name = api_data["sys"]["country"]

    temp = int(((api_data["main"]["temp"])-273.15))

    weather_desc = api_data["weather"][0]["description"]

    pressure = api_data["main"]["pressure"]

    humidity = api_data["main"]["humidity"]

    wind_speed = api_data["wind"]['speed']

    final_info = country_name + "\n" + date_time + "\n" + weather_desc + "\n" + str(temp) + "°C"
    final_data = "\n" + "Pressure : " + str(pressure) + "\n" + "Humidity : " + str(humidity) + "\n" + "Wind Speed : " + str(wind_speed)

    label1.config(text = final_info)
    label2.config(text = final_data)

box = tk.Tk()
box.geometry("500x500")
box.title("Weather Application")

textfield = tk.Entry(box , bg = "Grey" , justify = "center", font = ("poppins" ,35 , "bold"))
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', weather)

label1 = tk.Label(box , font = ("poppins" ,25 , "bold"))
label1.pack()
label2 = tk.Label(box , font = ("poppins" ,15 , "bold"))
label2.pack()

box.mainloop()