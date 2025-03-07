import requests
import os
import webbrowser

def city_mode():
    city = []
    postcode = []
    city = input("Which City would you like to check the weather for? ")
    url = 'http://api.weatherapi.com/v1/current.json?key=6dcf7d7344bf437fbc7171337241811&q='+city+'&aqi=no'



    response = requests.get(url)
    weather_json = response.json()

    temp = weather_json.get('current').get('temp_c')
    description = weather_json.get('current').get('condition').get('text')
    region = weather_json.get('location').get('region')
    weather_time = weather_json.get('location').get('localtime')
    wind_direction = weather_json.get('current').get('wind_dir')
    wind_speed = weather_json.get('current').get('wind_mph')

    print("Today's weather in " + city + ", " + region + " is ", description, 'and', temp, ' Degrees C\n')

    print(f'Wind conditions\n There is a {wind_direction} wind blowing at {wind_speed}\n')
    print("The time is " + weather_time)


def postcode_mode():
    city = []
    postcode = []
    postcode = input("Which Postcode would you like to check the weather for? ")
    url = 'http://api.weatherapi.com/v1/current.json?key=6dcf7d7344bf437fbc7171337241811&q='+postcode+'&aqi=no'



    response = requests.get(url)
    weather_json = response.json()

    temp = weather_json.get('current').get('temp_c')
    description = weather_json.get('current').get('condition').get('text')
    region = weather_json.get('location').get('region')
    weather_time = weather_json.get('location').get('localtime')
    wind_direction = weather_json.get('current').get('wind_dir')
    wind_speed = weather_json.get('current').get('wind_mph')

    print("Today's weather in " + city + ", " + region + " is ", description, 'and', temp, ' Degrees C\n')

    print(f'Wind conditions\n There is a {wind_direction} wind blowing at {wind_speed}\n')
    print("The time is " + weather_time)



def main_menu():
    app_mode = ()
    app_mode = (input("Would you like to enter a city or a postcode? \n a) Postcode \n b) City\n"))

    if app_mode == 'a':
        mode = city_mode()
        app_mode = []
        main_menu()
    elif app_mode == 'b':
        mode = postcode_mode()
        app_mode = []
        main_menu()


main_menu()
    
