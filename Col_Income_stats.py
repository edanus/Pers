import matplotlib.pyplot as plt
import numpy as np

# Data is based on national distribution, adjusted for each city's economy.
# Brackets are: <1, 1-2, 2-4, and >4 times the Minimum Wage (MW).
cities = {
    "Bogotá": [38, 35, 17, 10],
    "Medellín": [40, 36, 16, 8],
    "Barranquilla": [45, 38, 12, 5],
    "Pereira": [48, 39, 10, 3]
}

# Labels for the x-axis of the chart
mw_labels = ["<1 MW", "1-2 MW", "2-4 MW", ">4 MW"]
x_pos = np.arange(len(mw_labels))

# Loop through each city in our data dictionary
for city, data in cities.items():
    # Create a new figure for each chart to keep them separate
    plt.figure(figsize=(8, 5))
    
    # Create the bar chart
    plt.bar(x_pos, data, color='skyblue')
    
    # Add labels and a title for clarity
    plt.ylabel("Percentage of Workforce (%)")
    plt.xlabel("Monthly Salary Bracket (MW = Minimum Wage)")
    plt.title(f"Estimated Salary Distribution in {city}")
    plt.xticks(x_pos, mw_labels)
    plt.ylim(0, 55) # Set a consistent y-axis limit for easy comparison

    # Add the percentage number on top of each bar
    for i, v in enumerate(data):
        plt.text(x=i, y=v + 1, s=f"{v}%", ha='center')

    # Save the chart as a PNG image file
    plt.tight_layout()
    plt.savefig(f"salary_histogram_{city.lower()}.png")

print("Chart generation complete. Files saved.")