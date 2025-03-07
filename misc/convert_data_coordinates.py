## change data to co-ordinates and score ###
import os
import csv
import pandas as pd
import requests



def fetch_coords(authorities):
    try: 
        local_authority = authorities
        url = 'http://api.weatherapi.com/v1/current.json?key=6dcf7d7344bf437fbc7171337241811&q='+local_authority+'&aqi=no'
        response = requests.get(url)
        response.raise_for_status()
        la_json = response.json()

        exact_location_lat = la_json.get('location').get('lat')
        exact_location_long = la_json.get('location').get('lon')

        if exact_location_lat is None or exact_location_long is None:
            raise ValueError("Missing location data in API response")

        return f'{exact_location_lat}, {exact_location_long}'

    except requests.exceptions.RequestException as e:
        # Handle network-related errors (e.g., timeout, connection error)
        print(f"Error fetching data from API: {e}")
        return "0.0000, 0.0000"

    except AttributeError:
        # Handle cases where 'location' or 'lat/lon' is missing
        print("Error: API response structure is invalid or missing fields.")
        return "0.0000, 0.0000"

    except ValueError as e:
        # Handle custom validation errors
        print(f"Error: {e}")
        return "0.0000, 0.0000"

    except Exception as e:
        # Catch-all for any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return "0.0000, 0.0000"



coords_file_fields = ['authorities', 'coords']
exact_location_lat = []
exact_location_long = []

request_count = int()

with open('scored_file.csv', mode='r') as scored_file:
        csv_reader = csv.DictReader(scored_file)

        with open('coords_file.csv', mode='w') as coords_file:
                coords_file_writer = csv.DictWriter(coords_file, fieldnames=coords_file_fields, delimiter=',')
                coords_file_writer.writeheader()

                for line in csv_reader:
                    
                        del line['auth_code']
                        del line['Observation']
                        del line['Score']

                        authorities = line['authorities']

                        line['coords'] = fetch_coords(authorities)
                        request_count = request_count+1
                        print(f'{request_count} requests complete')

                        coords_file_writer.writerow(line)