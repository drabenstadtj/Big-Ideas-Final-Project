import json
import geojson
from shapely.geometry import shape, Point, MultiLineString

# Load GeoJSON data for neighborhoods
with open('neighborhoods.geojson') as f:
    geojson_data = json.load(f)

# Extract neighborhood polygons
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

# Read the CSV file containing latitude and longitude for parks
parks_data = []
with open('data\city-parks.csv', 'r') as file:
    next(file)  # Skip header
    for line in file:
        parts = line.strip().split(',')
        lat, lon = map(float, parts[-2:])
        parks_data.append((lat, lon))

# Create a dictionary to store parks count
parks_results = {"neighborhoods": []}

# Iterate through each park point
for lat, lon in parks_data:
    hood = is_point_within_polygon(lat, lon)
    if hood is not None:
        found = False
        for entry in parks_results["neighborhoods"]:
            if entry["name"] == hood:
                entry["parks"] += 1
                found = True
                break
        if not found:
            parks_results["neighborhoods"].append({"name": hood, "parks": 1})

# Read the CSV file containing latitude and longitude for prt-stops
prt_stops_data = []
with open('data\prt-stops.csv', 'r') as file:
    next(file)  # Skip header
    for line in file:
        parts = line.strip().split(',')
        lat, lon = map(float, parts[-2:])
        prt_stops_data.append((lat, lon))

# Create a dictionary to store prt-stops count
prt_stops_results = {"neighborhoods": []}

# Iterate through each prt-stop point
for lat, lon in prt_stops_data:
    hood = is_point_within_polygon(lat, lon)
    if hood is not None:
        found = False
        for entry in prt_stops_results["neighborhoods"]:
            if entry["name"] == hood:
                entry["prt-stops"] += 1
                found = True
                break
        if not found:
            prt_stops_results["neighborhoods"].append({"name": hood, "prt-stops": 1})

# Merge results
merged_results = {"neighborhoods": []}

# Merge parks_results and prt_stops_results
for park_entry, prt_stop_entry in zip(parks_results["neighborhoods"], prt_stops_results["neighborhoods"]):
    merged_entry = {"name": park_entry["name"], "parks": park_entry["parks"], "prt-stops": prt_stop_entry["prt-stops"]}
    merged_results["neighborhoods"].append(merged_entry)

# Load GeoJSON data for bikelanes
with open('data/2019-bike-lanes.geojson') as f:
    bikelanes_data = json.load(f)

# Initialize a dictionary to store lane lengths
bikelane_lengths = {hood_name: 0.0 for hood_name in hoods}

# Iterate over each bike lane feature
for feature in bikelanes_data['features']:
    bikelane_geometry = shape(feature['geometry'])
    # Iterate through each neighborhood
    for hood_name, polygon in zip(hoods, polygons):
        # Check if the bike lane intersects with the neighborhood polygon
        if bikelane_geometry.intersects(polygon):
            # Calculate the length of the intersection
            intersection = bikelane_geometry.intersection(polygon)
            bikelane_lengths[hood_name] += intersection.length

# Update merged_results with bike lane lengths
for entry in merged_results["neighborhoods"]:
    hood_name = entry["name"]
    entry["bikelane_length"] = bikelane_lengths[hood_name]

# Write the merged results to a JSON file
with open('neighborhoods-count.json', 'w') as outfile:
    json.dump(merged_results, outfile)

print("Results written to neighborhoods-count.json")
