import csv
import os

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
        
initiatives_path = input("Enter Initiatives Path: \n")
incidents_path = input("Enter Incidents path: \n")

return_IRN_from_initiative(initiatives_path, 'Initiative_Headline', 'IRNs') ##call return IRNs function#


##code below is to split IRN Rows

with open('combined_file.csv', mode='r') as infile, open('final_file.csv', mode='w', newline='') as outfile:
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






