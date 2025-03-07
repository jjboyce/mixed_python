import csv
import os

import split_IRN_rows

# Define the new fields to be added
new_fields = ['Start', 'Finish', 'Duration', 'Customer', 'Headline', 'Impact Summary', 'Mitigation', 'Priority', 'Service/Platform', 'Sub Platform', 'Source', 'Spares Issue', 'Spares Status']


# Open the existing CSV file in read mode
with open('final_file.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    # Get the header from the existing CSV file
    header = next(csv_reader)
    # Ensure the header is a list
    if isinstance(header, list):
        # Add the new fields to the header
        header.extend(new_fields)
    else:
        raise ValueError("Header is not a list")
    
    # Open a new CSV file in write mode
    with open('combined_report.csv', 'w', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        # Write the modified header to the new CSV file
        csv_writer.writerow(header)
        # Write the rest of the data to the new CSV file
        for row in csv_reader:
            csv_writer.writerow(row)
            

os.remove("final_file.csv")


            
        
    
    
