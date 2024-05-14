import smtplib

# Define the SMTP server and port
smtp_server = 'smtp.example.com'
port = 587

# Your email credentials
username = 'user@example.com'
password = 'password'

# Establish a connection to the SMTP server
server = smtplib.SMTP(smtp_server, port)
server.set_debuglevel(1)

# Start the connection
server.ehlo('example.com')  # Replace 'example.com' with your valid domain
# Secure the connection
server.starttls()

# Login to the server
server.login(username, password)

# Send an email
from_address = 'from@example.com'
to_address = 'to@example.com'
message = """\
Subject: Test Email

This is a test email.
"""
server.sendmail(from_address, to_address, message)

# Close the connection
server.quit()