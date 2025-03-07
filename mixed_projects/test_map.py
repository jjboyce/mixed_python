import requests
import os
import webbrowser
import html
import folium
from folium import Map
from folium.plugins import HeatMap
import pandas as pd
import csv

df = pd.read_csv('scored_coords_file.csv')

df[['latitude', 'longitude']] = df['coords'].str.split(',', expand=True)

df['latitude'] = df['latitude'].astype(float)
df['longitude'] = df['longitude'].astype(float)

# Create a base map
m = Map(location=[51.1801, -2.6237], zoom_start=8)

# Data: [latitude, longitude, weight]
data = df[['latitude', 'longitude']].values.tolist()

# Add a weighted HeatMap layer
HeatMap(data).add_to(m)

# Save to file
m.save("weighted_heatmap.html")