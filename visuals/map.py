import folium
import json
from branca.colormap import linear

# Load neighborhood data from JSON
with open('../composite_scores.json') as f:
    neighborhood_data = json.load(f)

# Create a dictionary mapping neighborhood names to their scores
neighborhood_scores = {neighborhood['name']: neighborhood for neighborhood in neighborhood_data}

# Load GeoJSON file containing neighborhood boundaries
with open('../data/neighborhoods.geojson') as f:
    geojson_data = json.load(f)

# Iterate over features in GeoJSON data
for feature in geojson_data['features']:
    # Extract neighborhood name from GeoJSON feature
    hood_name = feature['properties']['hood']
    # Check if the neighborhood name exists in the scores dictionary
    if hood_name in neighborhood_scores:
        # Retrieve the scores for the neighborhood
        scores = neighborhood_scores[hood_name]
        # Add the scores to the GeoJSON feature properties
        feature['properties'].update(scores)

# Create a Folium map centered at a specific location
m = folium.Map(location=[40.4406, -79.9959], zoom_start=12)

# Add GeoJSON data to the map with a custom name and style for composite score
folium.GeoJson(
    geojson_data,
    name='Composite Score',
    show=False,
    overlay=True,
    style_function=lambda feature: {
        'fillColor': linear.YlGnBu_09.scale(0, 1)(feature['properties'].get('composite_score', 0)),
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.6
    }
).add_to(m)

# Add GeoJSON data to the map with a custom name and style for bus stops
folium.GeoJson(
    geojson_data,
    name='Bus Stops',
    show=False,
    overlay=True,
    style_function=lambda feature: {
        'fillColor': linear.OrRd_09.scale(0, 1)(feature['properties'].get('prt_stops_normalized', 0)),
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.6
    }
).add_to(m)

# Add GeoJSON data to the map with a custom name and style for bike lane length
folium.GeoJson(
    geojson_data,
    name='Bike Lane Length',
    show=False,
    overlay=True,
    style_function=lambda feature: {
        'fillColor': linear.PuBuGn_09.scale(0, 1)(feature['properties'].get('bikelane_length_normalized', 0)),
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.6
    }
).add_to(m)

# Add GeoJSON data to the map with a custom name and style for parks
folium.GeoJson(
    geojson_data,
    name='Parks',
    show=False,
    overlay=True,
    style_function=lambda feature: {
        'fillColor': linear.YlOrRd_09.scale(0, 1)(feature['properties'].get('parks_normalized', 0)),
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.6
    }
).add_to(m)

# Add layer control to toggle the GeoJSON layers
folium.LayerControl().add_to(m)

# Save the map as an HTML file
m.save('neighborhood_map.html')
