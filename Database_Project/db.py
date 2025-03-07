## db pi project

import sqlite3
conn = sqlite3.connect("/Users/johnboyce/vs_code_projects/Database_Project/users.db")
cursor = conn.cursor()

option_chosen = input("What would you like to do?  \n1) View all users\n2) Add a User\n3) Remove a User\n4) Run Custom Query\n")

if option_chosen == "1":
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
    conn.close()

elif option_chosen == "2":
    name = input("Enter First Name: ")
    email = input("Enter email: ")
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (f"{name}", f"{email}"))
    conn.commit()
    conn.close()

elif option_chosen == "3":
    email = input("Enter the email of the user to remove: \n")
    cursor.execute(f"DELETE FROM users WHERE email='{email}'")
    conn.commit()
    conn.close()

elif option_chosen == "4":
    query_input = input("Enter Query:\n")
    cursor.execute(f"{query_input}")
    conn.commit()
    conn.close()

        