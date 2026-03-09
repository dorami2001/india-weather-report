
import requests
import json
import csv
import matplotlib.pyplot as plt
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")
cities = cities = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata",
          "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Bhubaneswar"]

all_weather = []

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={"REMOVED"}&units=metric"
    response = requests.get(url)
    data = response.json()
    print("Data fetched successfully")

    if data.get("main"):  
        weather_report = {
            "City": data["name"],
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"]
        }
        all_weather.append(weather_report)
    else:
        print(f"Failed to fetch data for {city}: {data.get('message')}")


sorted_weather = sorted(all_weather, key=lambda x: x["Temperature"], reverse=True)


with open("data/weather_data.json", "w") as f:
    json.dump(all_weather, f, indent=4)

print("JSON file is created")


with open("data/top5_cities_india.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Temperature (°C)", "Humidity (%)", "Weather"])
    for w in sorted_weather[:5]:
        writer.writerow([w["City"], w["Temperature"], w["Humidity"], w["Weather"]])

print("CSV file created: top5_cities_india.csv")

cities = []
temps = []

with open("data/top5_cities_india.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cities.append(row["City"])
        temps.append(float(row["Temperature (°C)"]))

plt.bar(cities, temps)
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Top 5 Hottest Cities in India")

plt.savefig("temperature_chart.png")

plt.show()

with open("data/all_cities_weather_india.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Temperature (°C)", "Humidity (%)", "Weather"])
    for w in all_weather:
        writer.writerow([w["City"], w["Temperature"], w["Humidity"], w["Weather"]])

print("CSV file created: all_cities_weather_india.csv")

