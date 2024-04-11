import json
import matplotlib.pyplot as plt

# Read JSON data from file
with open('neighborhoods-count.json', 'r') as file:
    neighborhoods_data = json.load(file)

# Extracting neighborhood names and PRT stop counts
neighborhood_names = [neighborhood["name"] for neighborhood in neighborhoods_data["neighborhoods"]]
prt_stop_counts = [neighborhood["prt-stops"] for neighborhood in neighborhoods_data["neighborhoods"]]

# Creating the bar chart
plt.figure(figsize=(10, 6))
plt.bar(neighborhood_names, prt_stop_counts, color='lightgreen')
plt.xlabel('Neighborhoods')
plt.ylabel('Number of PRT Stops')
plt.title('Number of PRT Stops in Each Neighborhood')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
