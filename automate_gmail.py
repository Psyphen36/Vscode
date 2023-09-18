import smtplib
import ssl
from email.message import EmailMessage

subject = 'Email From Python'
body = 'Test message from python to see it works or not'
email_sender = 'pythonprojectslearner@gmail.com'
email_receiver = 'pythonprojectslearner@gmail.com'

password = 'pythonprojects369'

message = EmailMessage()
message['From'] = email_sender
message['To'] = email_receiver
message['Subject'] = subject
message.set_content(body)

context = ssl.create_default_context()

print('Sending Email...')

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(email_sender, password)
    server.sendmail(email_sender, email_receiver, message.as_string())
print('Success!!')


