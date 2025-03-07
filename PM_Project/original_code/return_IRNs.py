import csv
import os

##function to return IRNs from Initiatives##
def return_IRN_from_initiative(file_path, field_name1, field_name2):
    try:
        with open(file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            if field_name1 not in csv_reader.fieldnames:
                print(f"Error: Field '{field_name1}' not found in the CSV file.")
                return
            
            if field_name2 not in csv_reader.fieldnames:
                print(f"Error: Field '{field_name2}' not found in the CSV file.")
                
            
            for line in csv_reader:
                print("Lines Returned")
                return(line[field_name1])
                return(line[field_name2])
    
                
                
    except FileNotFoundError:
        print(f"Error: file not found at '{file_path}'.")
        
    except Exception as e:
        print(f"An unexpected error occurred {e}")
        



return_IRN_from_initiative('initiatives.csv', 'Initiative_Headline', 'IRNs') ##call return IRNs function#

#with open('combined_problem.csv', 'w',  





