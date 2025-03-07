import csv
import re

# Function to remove non-standard characters (non-ASCII characters)
def remove_non_standard_characters(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)

# Try reading the file with multiple encodings
def read_csv_with_encoding(filename):
    encodings_to_try = ['utf-8', 'ISO-8859-1', 'utf-8-sig', 'latin1']
    for encoding in encodings_to_try:
        try:
            # Open file inside the try block to ensure it's only opened once successfully
            infile = open(filename, mode='r', newline='', encoding=encoding)
            return infile, encoding
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Unable to read file {filename} with any of the tried encodings.")

# Read the original CSV file and clean the data
input_file = "/Users/johnboyce/vs_code_projects/mixed_projects/addresses.csv"  # Change this to your input file
output_file = "cleaned_addresses.csv"  # This will be the new CSV file with cleaned data

# Attempt to read the file with a suitable encoding
try:
    infile, used_encoding = read_csv_with_encoding(input_file)
    print(f"File read successfully using {used_encoding} encoding.")
except ValueError as e:
    print(str(e))
    exit(1)

# Now, with the file properly opened, use csv.DictReader
reader = csv.DictReader(infile)

# Get the fieldnames (columns) from the original file
fieldnames = reader.fieldnames

# Create a list to store the cleaned rows
cleaned_rows = []

for row in reader:
    # Clean each field in the row
    cleaned_row = {key: remove_non_standard_characters(value) for key, value in row.items()}
    cleaned_rows.append(cleaned_row)

# Write the cleaned data to a new CSV file
with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    # Write header
    writer.writeheader()
    
    # Write cleaned rows
    writer.writerows(cleaned_rows)

print(f"File has been cleaned and saved as '{output_file}'")

# Close the input file after processing
infile.close()