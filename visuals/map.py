import folium
import json
import pandas as pd

# Load GeoJSON files
with open('data/neighborhoods.geojson') as f:
    neighborhoods = json.load(f)

with open('data/2019-bike-lanes.geojson') as f:
    bikelanes = json.load(f)

# Create a map centered at a specific location
m = folium.Map(location=[40.451651, -79.940531], zoom_start=10)


# Define a list of colors
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']  # Add more colors if needed

# Assign a color to each feature in data1
for idx, feature in enumerate(neighborhoods['features']):
    color = colors[idx % len(colors)]
    folium.GeoJson(feature, name=f'Data 1 - Feature {idx}', 
                   style_function=lambda x, color=color: {'fillColor': color, 'color': 'none', 'weight': 2}).add_to(m)


# # Add GeoJSON data to the map with different colors and outline colors
# folium.GeoJson(neighborhoods, name='Data 1', 
#                style_function=lambda x: {'fillColor': 'green', 'color': 'white', 'weight': 1}, 
#                highlight_function=lambda x: {'weight': 3}).add_to(m)

folium.GeoJson(bikelanes, name='Data 2', 
               style_function=lambda x: { 'color': 'red', 'weight': 2}, 
               highlight_function=lambda x: {'weight': 3}).add_to(m)

# Load the CSV file
df = pd.read_csv('data\city-parks.csv')

# Iterate through each row in the dataframe
for index, row in df.iterrows():
    # Extract latitude and longitude
    lat, lon = row['latitude'], row['longitude']
    # Add a marker for each park
    folium.Marker(location=[lat, lon], tooltip=row['name']).add_to(m)

# # Load the CSV file
# df = pd.read_csv('data\prt-stops.csv')

# # Iterate through each row in the dataframe
# for index, row in df.iterrows():
#     # Extract latitude and longitude
#     lat, lon = row['latitude'], row['longitude']
#     # Customize marker size and color
#     folium.Circle(location=[lat, lon], radius=1, color='grey', fill_color='red', fill_opacity=0.7).add_to(m)

# Add Layer Control to toggle between layers
folium.LayerControl().add_to(m)

# Save the map as an HTML file
m.save('map_with_overlay.html')
