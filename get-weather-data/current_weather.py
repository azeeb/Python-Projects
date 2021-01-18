import requests

#Api key
api_key = "####"

#Store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#Give city Name
city_name = input("Enter city name: ")

#Full url to fetch weather data
complete_url = base_url + "q=" + city_name + "&units=metric"+ "&appid=" + api_key

#Fetching the data
response = requests.get(complete_url)
x = response.json()

#displaying useful data
if x["cod"] != "404":
    y = x['main']
    z = x["weather"]
    print("Temperature in (celsius) = " + str(y["temp"])
            + "\n Feels Like = " + str(y["feels_like"])
            + "\n Humidity (%) = " + str(y["humidity"])
            + "\n Description = " + str(z[0]["description"])
            + "\n Wind Speed (m/s) = " + str(x["wind"]["speed"]) 
            + "\n Country = " + str(x["sys"]["country"]))
else:
    print("City not found")


