import os

filename = '/Users/johnboyce/vs_code_projects/PM_Data_project/some_text.txt'
os.path.exists(filename)

if os.path.exists(filename):
    os.remove(filename)
    print(f'File {filename} has been removed successfully')
else:
    print("File doesn't exist")

    