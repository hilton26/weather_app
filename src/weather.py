import requests
from dotenv import load_dotenv  # to load environment variables in .env file
import os

load_dotenv()  # load environment variables from .env file
API_KEY = os.getenv("API_KEY")  # get API key from environment variable


def get_current_weather():
    print("\n**** Get Current Weather Conditions ****\n")

    city = input("\nPlease enter a city name: \n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)

    weather_data = requests.get(request_url).json()

    print(weather_data)


get_current_weather()
