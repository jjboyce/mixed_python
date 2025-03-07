## address cleaner ##

import csv

# Define the input and output file names
input_file = '/Users/johnboyce/vs_code_projects/mixed_projects/bramhall_addresses.csv'
output_file = 'cleaned_bm_addresses.csv'

# Open the input CSV file and read the data
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Process each row
    for row in reader:
        # Get the original address
        address = row[0]
        
        # Add "6 " at the start of the address and add a space before "SK7"
        new_address = "6 " + address.replace('SK7', ' SK7')
        
        # Write the updated row to the output CSV
        writer.writerow([new_address])

print(f"CSV data has been amended and saved to {output_file}")