### remove icloud emails  ###
import csv

# Input and output file names
input_csv = "cleaned_emails.csv"
output_csv = "filtered_email_headers.csv"

# Email to exclude
exclude_email = "johnjboyce01@icloud.com"

# Read input CSV and filter out unwanted rows
filtered_data = []
with open(input_csv, "r", encoding="utf-8") as infile:
    reader = csv.reader(infile)
    headers = next(reader)  # Read the header row
    filtered_data.append(headers)  # Keep the headers

    for row in reader:
        email_to = row[1]  # "To" column
        if email_to.lower() != exclude_email.lower():  # Case-insensitive comparison
            filtered_data.append(row)

# Save the filtered data to a new CSV file
with open(output_csv, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(filtered_data)

print(f"Filtered data saved to {output_csv}")