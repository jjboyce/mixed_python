### test code for adding missing data to Combined Report ###
import csv
import os
import pandas as pd

combined_report = input("Where is the incomplete data?:\n")
incident_data = input("Where is the complete Incident Data?:\n")

with open(incident_data, 'w') as read_obj:
    csv_reader = csv.reader(read_obj)
    header = next(csv_reader)
    next(csv_reader)
    


with open(combined_report, 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    header = next(csv_reader)
    next(csv_reader)
    for row in csv_reader:
        

    
    

    
    
    
    
    
    
    
    
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
        
###   os.remove("IRN_List.csv")