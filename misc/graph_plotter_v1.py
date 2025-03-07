import pandas as pd
import matplotlib.pyplot as plt


# Step 1: Load the CSV data
csv_file = input("Where is the data? \n")  # Replace with your CSV file path
data = pd.read_csv(csv_file)

# Step 2: Group data by a specific category
# Assuming the category column is named "Category" and we count occurrences
grouped_data = data['Spares Status'].value_counts()

# Step 3: Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution by Category')
plt.show()
