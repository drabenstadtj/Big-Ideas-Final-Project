import json
import csv

# Load GeoJSON data
with open('data\prt-stops.geojson', 'r') as f:
    data = json.load(f)

# Extract necessary information
rows = []
for index, feature in enumerate(data['features']):
    latitude = feature['properties']['Latitude']
    longitude = feature['properties']['Longitude']
    rows.append([index, latitude, longitude])

# Write to CSV
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Index', 'Latitude', 'Longitude'])
    writer.writerows(rows)

print("CSV file created successfully.")
