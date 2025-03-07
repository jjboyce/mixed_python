import requests
import os
import webbrowser
import html
import folium


def get_weather(location):
    url = 'http://api.weatherapi.com/v1/current.json?key=6dcf7d7344bf437fbc7171337241811&q='+location+'&aqi=no'


    response = requests.get(url)
    weather_json = response.json()

    temp = weather_json.get('current').get('temp_c')
    description = weather_json.get('current').get('condition').get('text')
    region = weather_json.get('location').get('region')
    weather_time = weather_json.get('location').get('localtime')
    wind_direction = weather_json.get('current').get('wind_dir')
    wind_speed = weather_json.get('current').get('wind_mph')
    confirmed_location = weather_json.get('location').get('name')
    exact_location_lat = weather_json.get('location').get('lat')
    exact_location_long = weather_json.get('location').get('lon')

    print(f"\nToday's weather in {confirmed_location} ({region}) is {description} : {temp}C\n")
    print(f'There is a {wind_direction} wind blowing at {wind_speed}\n')
    print(weather_time)

    the_weather = f'{description}, {temp}C'
    the_wind = f'{wind_direction}, {wind_speed}'
    the_time = weather_time

    popup_content = f'{confirmed_location}, {the_weather}'

    
    # Create a map
    my_map = folium.Map(location=[exact_location_lat, exact_location_long], zoom_start=7)

    # Add a marker
    folium.Marker([exact_location_lat, exact_location_long], popup=popup_content).add_to(my_map)

    # Save to file
    my_map.save("map.html")


user_location = input("Enter Location: \n")
get_weather(user_location)




