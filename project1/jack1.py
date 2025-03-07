##Variables##

from datetime import datetime

user_name = ()
tenant_names = ["Jack", "James"]
pet_names = ["Shadow","Trixie"]
num_pets = int(len(pet_names))
property_postcode = "SK9 2NU"
tenant_pin = int("9011")
now = datetime.now()
login_status = ""

######## main code  ######

user_name = input("Please tell me your name: ")
qr_no_pets = int(input("How many pets do you have? "))
pin_input = int(input("What is your tenant PIN? "))
pet_challenge = input("Please name one of your pets: ")

if qr_no_pets == num_pets and pin_input == tenant_pin and user_name in tenant_names and pet_challenge in pet_names:
    print("Thank you. Please Proceed")
    login_status = "PASSED"
    print("""
       _____
     | O   O |
     |   ^   |
     |  ---  |
       _____
    """)

else:
    print("Sorry, we cannot proceed. Please check your email for further details")
    login_status = "FAILED"

logfilename = now.strftime("%Y_%m_%d %H_%M_%S") + '.txt'
logfile = open(logfilename, "x")
logfile.write("\n" + user_name + " attempted to log in at " + now.strftime("%Y-%m-%d %H:%M:%S") + " " + " and " + login_status + " security")
logfile.close()





