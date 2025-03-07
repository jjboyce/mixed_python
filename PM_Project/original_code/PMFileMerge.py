import csv
import os

#incidents_file = input("Enter Path of Incidents File:\n")
initiatives_file = input("Enter Path of Initiatives File:\n")
merged_file = []

incident_current_headers = ['RowID', 'IRN', 'FyYear' , 'FyQuarter' , 'Date', 'Start', 'Finish', 'Duration', 'Actions', 'AR', 'Count' , 'Customer', 'Customer Scorecard' , 'Customer Non-Scorecard' , 'ElementComponent', 'Headline', 'Impact Summary', 'Incident Type', 'Mitigation', 'Open Actions', 'PIR Status', 'PIR Status Simple', 'PIRID', 'PIRUpdate', 'PIRUpdatedOn', 'POR', 'Priority', 'Problem Manager', 'Risk', 'Root Cause', 'Scorecard', 'Service/Platform', 'Sub Platform', 'Source', 'Spares Issue', 'Spares Status', 'Status', 'Wk_No', 'S2N Include', 'S2N Result', 'S2N Fail Reason MC', 'S2N Fail Reason SC', 'SensitiveYN', 'Permission', 'IncidentSrc', 'PM Review', 'Sensitive', 'Team', 'PIR Type', 'Near_Miss', 'S2N Status', 'Problem_Record_Priority']
incident_desired_headers = ['IRN', 'Start', 'Finish', 'Duration', 'Customer', 'Headline', 'Impact Summary', 'Mitigation', 'Priority', 'Service/Platform', 'Sub Platform', 'Source', 'Spares Issue', 'Spares Status']



##function to return named field from CSV
def return_named_field_from_csv(file_path, field_name):
    try:
        with open(file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            if field_name not in csv_reader.fieldnames:
                print(f"Error: Field '{field_name}' not found in the CSV file.")
                return
            
            print(f"Values of field {field_name}:")
            for line in csv_reader:
                print(line[field_name])
    
    except FileNotFoundError:
        print(f"Error: file not found at '{file_path}'.")
        
    except Exception as e:
        print(f"An unexpected error occurred {e}")



##for given row in initiatives file, return entry in IRN

return_named_field_from_csv(input("Enter Initiative location"), input("Input the field to return: "))
print()

    
    
    
    
    
    
    
    #field_to_print = 'Initiative_Headline'
    #fieldnames = ['Owner', 'Service', 'Initiative_Headline', 'Initiative_Description', 'Benefit', 'Reliability_Impact', 'Progress_Notes', 'Due_Date', 'Status', 'Volume', 'ID', 'Owner_EIN', 'Initiative_fk', 'Deleted', 'IRNs']
    
    #if field_to_print not in csv_reader.fieldnames:
        #print(f"Error: Field {field_to_print} not found in the file")
    #else:
        #for row in csv_reader:
            #return(row[field_to_print])



        
    

    
    


        
    
    
    
    



        
  
    
    

    
#with open('output_file.csv', 'w') as merged_file:
    #sv_writer = csv.writer(merged_file)
            
            
    
    
   # for line in csv_reader:#
    #    print(line)#
    

