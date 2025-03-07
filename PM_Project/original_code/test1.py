import csv

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