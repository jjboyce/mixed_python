import imaplib
import email
import csv
import datetime
from email.header import decode_header

# Email account details
IMAP_SERVER = "imap.mail.me.com"  # Change this for different providers
EMAIL_ACCOUNT = "johnjboyce01@icloud.com"
EMAIL_PASSWORD = "jfik-cjzo-lxph-pgsy"

# Connect to the IMAP server securely using SSL
try:
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, 993)  # Explicit SSL connection
    mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
    print("Login successful!")
except imaplib.IMAP4.error as e:
    print(f"Login failed: {e}")
    exit()

# Select the inbox folder
mail.select("inbox")

# Calculate the date 6 months ago
six_months_ago = (datetime.datetime.now() - datetime.timedelta(days=100)).strftime("%d-%b-%Y")

# Search for emails received in the last 6 months
print("Downloading email headers.")
search_criteria = f"SINCE {six_months_ago}"
result, data = mail.search(None, search_criteria)

if result != "OK":
    print("No emails found.")
    mail.logout()
    exit()

email_ids = data[0].split()
emails = []

# Fetch email headers securely
for email_id in email_ids:
    result, msg_data = mail.fetch(email_id, "(RFC822.HEADER)")
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            email_date = msg["Date"]
            email_to = msg["To"]
            email_from = msg["From"]

            # Decode email headers safely
            email_from = decode_header(email_from)[0][0] if email_from else "Unknown"
            email_to = decode_header(email_to)[0][0] if email_to else "Unknown"
            email_date = decode_header(email_date)[0][0] if email_date else "Unknown"

            if isinstance(email_from, bytes):
                email_from = email_from.decode(errors="ignore")
            if isinstance(email_to, bytes):
                email_to = email_to.decode(errors="ignore")
            if isinstance(email_date, bytes):
                email_date = email_date.decode(errors="ignore")

            emails.append([email_date, email_to, email_from])

# Save to CSV
csv_filename = "inbox.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "To", "From"])
    writer.writerows(emails)

print(f"Email headers saved to {csv_filename}")

# Logout and close the connection securely
mail.logout()