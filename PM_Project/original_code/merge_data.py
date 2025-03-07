### alternative merge function 

import pandas as pd

raw_combined_report = input("Where is the report with the missing data?\n")
incident_data = input("Where is the incident data?\n")

# Load the two CSV files into DataFrames
combined_report = pd.read_csv(raw_combined_report)
incident_data = pd.read_csv(incident_data)

# Specify the key columns in each file
irn_combined_report = 'IRNs'  # Key column in File 1
irn_incident_data = 'IRN'  # Key column in File 2
columns_to_complete = ['Start','Finish','Duration','Customer','Headline','Impact Summary','Mitigation','Priority','Service/Platform','Sub Platform','Source','Spares Issue','Spares Status']

# Merge the two DataFrames using different key column names
merge_columns = [irn_incident_data] + columns_to_complete
merged = combined_report.merge(incident_data[merge_columns], 
                     left_on=irn_combined_report, 
                     right_on=irn_incident_data, 
                     how='left')

# Fill missing values for each specified column
for col in columns_to_complete:
    merged[col] = merged[f'{col}_x'].combine_first(merged[f'{col}_y'])

# Drop unnecessary intermediate columns
drop_columns = [f'{col}_x' for col in columns_to_complete] + [f'{col}_y' for col in columns_to_complete] + [irn_incident_data]
merged = merged.drop(columns=drop_columns)

# Save the updated DataFrame back to a new CSV file
merged.to_csv('updated_file1.csv', index=False)

print("Missing data has been filled and saved to 'updated_file1.csv'.")