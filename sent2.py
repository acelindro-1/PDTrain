import smtplib, ssl

port = 465  # For SSL

password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

sender_email = "electronicwall17@gmail.com"
receiver_email = "its.cedierecamara@gmail.com"  # Replace with recipient email address
message = """\
Subject: Test Email
This is a test email sent from Python."""

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as smtp:
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, receiver_email, message)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")

## INPUT PASSWORD: wwgj ktid hwbm ewcj
