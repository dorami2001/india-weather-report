# India Weather Data Project 🌤️

## Overview
This Python project fetches current weather data for multiple major cities in India using the openWeatherMap API.  

The project demonstrates:  
- Working with APIs in Python  
- JSON data handling  
- CSV file generation  
- Sorting data based on a specific metric (temperature)  

---

## Features
1. Fetch weather data for 10 major Indian cities: Delhi, Mumbai, Bangalore, Chennai, Kolkata, Hyderabad, Pune, Ahmedabad, Jaipur, Bhubaneswar.  
2. Save all data to a JSON file (`weather_data.json`).  
3. Create CSV files:  
   - `all_cities_weather_india.csv` → all cities  
   - `top5_cities_india.csv` → top 5 hottest cities in India  
4. Sort cities by temperature to identify the hottest regions.  

---

## Tech Stack
- Language: Python 3  
- Libraries: `requests`, `json`, `csv`  
- API: OpenWeatherMap  

---

## Setup Instructions

1. Clone the repository
'''bash
git clone <your_github_repo_url>
cd <repo_folder>