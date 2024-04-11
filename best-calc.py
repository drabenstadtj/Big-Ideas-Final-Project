import json 
import numpy as np

# Read JSON data from file
with open('processed data/neighborhoods-count.json', 'r') as file:
    neighborhoods_data = json.load(file)

neighborhoods = neighborhoods_data['neighborhoods']

# Normalize the data
max_parks = max(neighborhood['parks'] for neighborhood in neighborhoods)
max_prt_stops = max(neighborhood['prt-stops'] for neighborhood in neighborhoods)
max_bikelane_length = max(neighborhood['bikelane_length'] for neighborhood in neighborhoods)



for neighborhood in neighborhoods:
    neighborhood['parks_normalized'] = neighborhood['parks'] / max_parks
    neighborhood['prt_stops_normalized'] = neighborhood['prt-stops'] / max_prt_stops
    neighborhood['bikelane_length_normalized'] = neighborhood['bikelane_length'] / max_bikelane_length

# Assign weights 
weights = {
    'parks': .3,
    'prt_stops': .4,
    'bikelane_length': 0.3
}

# Calculate composite score
for neighborhood in neighborhoods:
    neighborhood['composite_score'] = (
        weights['parks'] * neighborhood['parks_normalized'] +
        weights['prt_stops'] * neighborhood['prt_stops_normalized'] +
        weights['bikelane_length'] * neighborhood['bikelane_length_normalized']
    )


# Write composite scores
with open('composite_scores.json', 'w') as json_file:
    json.dump(neighborhoods, json_file, indent=4)

# Find the best neighborhood
best_neighborhood = max(neighborhoods, key=lambda x: x['composite_score'])

print("Best neighborhood:", best_neighborhood['name'])
print("Composite score:", best_neighborhood['composite_score'])
