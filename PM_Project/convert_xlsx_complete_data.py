import csv
import openpyxl
from openpyxl import Workbook
import PM_Project.original_code.create_combined_report as create_combined_report

wb = Workbook()
ws = wb.active

with open('combined_report.csv') as combined_report:
    reader = csv.reader(combined_report, delimiter=',')
    for row in reader:
        ws.append(row)

      
wb.save('complete_report.xlsx')

excel_path = 'complete_report.xlsx'
wb = openpyxl.load_workbook(excel_path)
sheet = wb.active

# Load the CSV file into a dictionary for quick lookup
csv_path = 'path_to_your_csv_file.csv'
lookup_dict = {}
with open(csv_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        lookup_dict[row['IRNs']] = row['Value']  # Assuming the CSV has columns 'Key' and 'Value