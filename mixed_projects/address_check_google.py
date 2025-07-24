import requests
from PIL import Image
from io import BytesIO
import os
import csv

# Replace with your actual API key
API_KEY = "APIKEY"
BASE_URL = "https://maps.googleapis.com/maps/api/streetview"

# Create a folder to store images
output_folder = "streetview_images"
os.makedirs(output_folder, exist_ok=True)

# Function to fetch the Street View static image for a given address
def get_streetview_image(address, size="600x400", heading=0, pitch=0, fov=90):
    params = {
        "size": size,
        "location": address,
        "heading": heading,  # Angle of view (0 to 360)
        "pitch": pitch,  # Tilt of the camera (-90 to 90)
        "fov": fov,  # Field of view (0 to 120)
        "key": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        print(f"Failed to fetch street view for {address}. Status code: {response.status_code}")
        return None

# Read addresses from the CSV file
csv_file = "/Users/johnboyce/vs_code_projects/cleaned_bm_addresses.csv"
addresses = []
with open(csv_file, newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        addresses.append(row['Address'])

# Generate HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Street View Images</title>
</head>
<body>
    <h1>Street View Images</h1>
    <ul>
"""

# Iterate through addresses and generate street view images
for address in addresses:
    image = get_streetview_image(address)
    if image:
        # Save the image to the output folder
        image_filename = f"{address.replace(' ', '_').replace(',', '')}.png"
        image_path = os.path.join(output_folder, image_filename)
        image.save(image_path)
        
        # Add the address and image to the HTML content
        html_content += f"""
        <li>
            <h3>{address}</h3>
            <img src="{image_path}" alt="Street View of {address}" style="width:600px;height:400px;">
        </li>
        """

# Finish the HTML content
html_content += """
    </ul>
</body>
</html>
"""

# Save the HTML file
html_file = "streetview_images.html"
with open(html_file, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"HTML file '{html_file}' generated successfully!")
