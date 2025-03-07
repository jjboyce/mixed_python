## budget manager ##

import sqlite3
from datetime import date
conn = sqlite3.connect("/Users/johnboyce/vs_code_projects/budget_manager/budget.db")
cursor = conn.cursor()

today = date.today()


## function to add new transaction ##
def add_transaction(description, amount, outgoing, paidflag):
    today = date.today()
    cursor.execute(f"INSERT INTO {month_selected} (date, description, amount, outgoing, paidflag) VALUES (?, ?, ?, ?, ?)", (f"{today}",f"{description}", f"{amount}", f"{outgoing}", f"{paidflag}"))
    conn.commit()
    audit_entry = f"£{amount} transaction for {description} added"
    audit_update(audit_entry)
    print(audit_entry)

## function to delete a transaction ##
def delete_transaction(id):
    cursor.execute(f"DELETE FROM {month_selected} WHERE id='{id}'")
    conn.commit()
    audit_entry = f"Transaction {id} Deleted"
    audit_update(audit_entry)
    print(audit_entry)

## function to mark as paid ##
def mark_paid(id):
    cursor.execute(f"UPDATE {month_selected} SET paidflag='True' WHERE id='{id}'")
    conn.commit()
    cursor.execute(f"UPDATE {month_selected} SET paidflagupdated='{today}' WHERE id='{id}'")
    conn.commit()
    audit_entry = f"Transaction {id} marked as paid."
    audit_update(audit_entry)
    print(audit_entry)

## function to create a new table ##
def create_month(month):
    create_table_query = f"""
    CREATE TABLE {month} (
    id INTEGER PRIMARY KEY,
    date DATE,
    description TEXT,
    amount INTEGER,
    outgoing BOOL,
    paidflag BOOL,
    paidflagupdated DATE
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    audit_entry = f"Table created for {month}"
    audit_update(audit_entry)
    print(audit_entry)


### function to delete a table - option 6 ###
def delete_month(month):
    cursor.execute(f"DROP TABLE {month}")
    conn.commit()
    audit_entry = f"{month} table deleted"
    audit_update(audit_entry)
    print(audit_entry)


### add to audit table ###

def audit_update(audit_entry):
    cursor.execute(f"INSERT INTO audit (date, comment) VALUES (?, ?)", (f"{today}",f"{audit_entry}"))
    conn.commit()
    conn.close()


month_selected = input("Which month would you like to Select?\n")

option_chosen = input("What would you like to do? \n1) View all transactions\n2)Enter a new transaction\n3)Delete a transaction\n4)Mark as paid\n5)Create a new month\n")

if option_chosen == "1":
    cursor.execute(f"SELECT * FROM {month_selected}")
    print(cursor.fetchall())
    conn.close()

elif option_chosen == "2":
    description = input("Enter transaction Description: \n")
    amount = input("How much is it?\n")
    outgoing = input("Is this an outgoing? Y/N \n")
    if outgoing == "Y":
        outgoing = "True"
    elif outgoing == "N":
        outgoing = "False"

    paidflag = input("Has this been paid yet?  Y/N \n")
    if paidflag == "Y":
        paidflag = "True"
    elif paidflag == "N":
        paidflag = "False"

    add_transaction(description, amount, outgoing, paidflag)

elif option_chosen == "3":
    id = input("What is the transaction ID to delete?")
    delete_transaction(id)

elif option_chosen == "4":
    id = input("What is the transaction ID to mark as paid?")
    cursor.execute(f"SELECT * FROM {month_selected} WHERE id={id}")
    print(cursor.fetchall())
    confirm_pay = input("Mark this as paid?\n")
    if mark_paid == "Y":
        mark_paid(id)
        conn.close()
    else:
        exit()

elif option_chosen == "5":
    month = input("Which month would you like to begin?\n")
    create_month(month)

elif option_chosen == "6":
    month = input("Which month would you like to DELETE?\n")
    delete_month(month)

