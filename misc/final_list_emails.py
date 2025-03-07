import csv
import re

# Input and output file names
input_csv = "inbox.csv"
output_csv = "final_email_list.csv"

# Common TLDs to exclude
tlds_to_exclude = {".com", ".co.uk", ".org", ".net", ".edu", ".gov", ".io", ".ai", ".us"}

def extract_domain(email):
    """Extracts domain from email, removing common TLDs."""
    match = re.search(r'@([\w.-]+)', email)  # Find domain after '@'
    if match:
        domain = match.group(1)

        # Remove common TLDs
        parts = domain.split('.')
        if len(parts) > 1 and "." + parts[-1] in tlds_to_exclude:
            domain = ".".join(parts[:-1])  # Remove last part if it's a common TLD
        
        return domain
    return "Unknown"

# Read input CSV and process data
cleaned_data = []
with open(input_csv, "r", encoding="utf-8") as infile:
    reader = csv.reader(infile)
    headers = next(reader)  # Read header row
    cleaned_data.append(["Date", "To", "From (Domain Only)"])  # New header

    for row in reader:
        email_date, email_to, email_from = row
        domain = extract_domain(email_from)  # Extract domain from "From" field
        cleaned_data.append([email_date, email_to, domain])

# Save to a new CSV file
with open(output_csv, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(cleaned_data)

print(f"Processed data saved to {output_csv}")