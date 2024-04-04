import json
from shapely.geometry import shape, Point

# Load GeoJSON data
with open('your_geojson_file.geojson') as f:
    geojson_data = json.load(f)

# Iterate through features and create Polygon objects
polygons = []
for feature in geojson_data['features']:
    polygon = shape(feature['geometry'])
    polygons.append(polygon)

# Define a function to check if a point is within any polygon
def is_point_within_polygon(lat, lon):
    point = Point(lon, lat)
    for polygon in polygons:
        if polygon.contains(point):
            return True
    return False

# Example latitude and longitude
lat = 37.7749
lon = -122.4194

# Check if the point is within any polygon
if is_point_within_polygon(lat, lon):
    print("The point is within the GeoJSON area.")
else:
    print("The point is not within the GeoJSON area.")
