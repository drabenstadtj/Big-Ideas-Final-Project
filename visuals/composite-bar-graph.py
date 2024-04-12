import json
import matplotlib.pyplot as plt

# Read JSON data from file
with open('data\processed data\composite_scores.json', 'r') as file:
    neighborhoods_data = json.load(file)


# Sort neighborhoods by ascending composite score
neighborhoods_data_sorted = sorted(neighborhoods_data, key=lambda x: x['composite_score'])

# Extracting names and composite scores of the top 10 neighborhoods
top_10_neighborhoods = neighborhoods_data_sorted[-10:]
neighborhood_names = [neighborhood["name"] for neighborhood in top_10_neighborhoods]
composite_scores = [neighborhood["composite_score"] for neighborhood in top_10_neighborhoods]

# Creating the bar graph
plt.figure(figsize=(10, 6))
plt.bar(neighborhood_names, composite_scores, color='skyblue')
plt.xlabel('Neighborhoods')
plt.ylabel('Composite Score')
plt.title('Top 10 Neighborhoods with Highest Composite Scores')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()