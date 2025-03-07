### Test Combined Code ###
import csv
import os
import pandas as pd

##function to return IRNs and Initiative Headline from Initiatives##

initiative_fields = ['Owner', 'Service', 'Initiative_Headline', 'Initiative_Description', 'Benefit', 'Reliability_Impact', 'Progress_Notes', 'Due_Date', 'Status', 'Volume', 'ID', 'Owner_EIN', 'Initiatives_fk', 'Deleted', 'IRNs']
short_initiative_fields = ['Initiative_Headline', 'IRNs']  ## required fields in output file

def return_IRN_from_initiative(file_path, field_name1, field_name2):
    try:
        with open(file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            if field_name1 not in csv_reader.fieldnames:
                print(f"Error: Field '{field_name1}' not found in the CSV file.")
                
            if field_name2 not in csv_reader.fieldnames:
                print(f"Error: Field '{field_name2}' not found in the CSV file.")    
            
            with open('combined_file.csv', 'w', newline='') as combined_file:
                combined_file_writer = csv.DictWriter(combined_file, fieldnames=short_initiative_fields, delimiter=',')
                combined_file_writer.writeheader() 
                                    
                for line in csv_reader: ##deletes non-needed fields##
                    del line['Owner']
                    del line['Service']
                    del line['Initiative_Description']
                    del line['Benefit']
                    del line['Reliability_Impact']
                    del line['Progress_Notes']
                    del line['Due_Date']
                    del line['Status']
                    del line['Volume']
                    del line['ID']
                    del line['Owner_EIN']
                    del line['Initiatives_fk']
                    del line['Deleted']
                                
                    combined_file_writer.writerow(line)

                    
    except FileNotFoundError:
        print(f"Error: file not found at '{file_path}'.")
        
    except Exception as e:
        print(f"An unexpected error occurred {e}")

##block of code to prompt for initiatives path and call function to return only initiative header and IRNs

initiatives_path = input("Enter Initiatives Path: \n")   ### input paths to initiatives and incidents here ###
return_IRN_from_initiative(initiatives_path, 'Initiative_Headline', 'IRNs') ## call return IRNs function#

incidents_path = input("Enter Incidents path: \n")

###block of code to separate IRNs into individual lines###

##code below separates the Incidents listed in Initiatives into individual records###

with open('combined_file.csv', mode='r') as infile, open('IRN_List.csv', mode='w', newline='') as outfile:
    csv_reader = csv.DictReader(infile)
    fieldnames = ['IRNs', 'Initiative_Headline']
    csv_writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    
    for row in csv_reader:
        irns_values = row['IRNs'].split(',')  # Replace 'IRNs' with the actual field name
        initiative_headline = row['Initiative_Headline']  # Replace 'Initiative_Headline' with the actual field name
        for irn in irns_values:
            csv_writer.writerow({'IRNs': irn, 'Initiative_Headline': initiative_headline})
            
            
os.remove("combined_file.csv")
print("\nIncident Records Created...\n")


#####   WIP code to add detailed columns from Incidents Spreadsheet ###

# Define the new fields to be added
new_fields = ['Start', 'Finish', 'Duration', 'Customer', 'Headline', 'Impact Summary', 'Mitigation', 'Priority', 'Service/Platform', 'Sub Platform', 'Source', 'Spares Issue', 'Spares Status']


# Open the existing CSV file in read mode
with open('IRN_List.csv', 'r') as read_obj:
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
            
os.remove("IRN_List.csv")

