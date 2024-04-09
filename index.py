import json
from shapely.geometry import shape, Point

# Load GeoJSON data
with open('neighborhoods.geojson') as f:
    geojson_data = json.load(f)

# Iterate through features and create Polygon objects
polygons = []
hoods = []
for feature in geojson_data['features']:
    polygon = shape(feature['geometry'])
    polygons.append(polygon)
    hoods.append(feature['properties']['hood'])

# Define a function to check if a point is within any polygon
def is_point_within_polygon(lat, lon):
    point = Point(lon, lat)
    for i, polygon in enumerate(polygons):
        if polygon.contains(point):
            return hoods[i]
    return None

# Example latitude and longitude
lat = 40.453902
lon = -79.928225


# Check if the point is within any polygon
hood = is_point_within_polygon(lat, lon)
if hood is not None:
    print(f"The point is within the GeoJSON area in the neighborhood: {hood}.")
else:
    print("The point is not within the GeoJSON area.")
    