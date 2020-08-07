import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#Here i set my email and password in an environment variable(the password is the special 16 character one given by google for setting up an app to by pass the two factor authentication
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')  # If you don't want to set an environment variable just set EMAIL_ADDRESS equal to your actual email address as a string. Same with the password
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

msg = MIMEMultipart()
msg['Subject'] = 'Basketball stats'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS

body = 'Hi there! This is your weekly E-mail.' #Body of the email
msg.attach(MIMEText(body,'plain'))  # sets the colour of the text and attaching the text to the the email

filename='Data.csv'         # the name of the file being attached to the e-mail
attachment  =open(filename,'rb')     #Reading the file

part = MIMEBase('application','octet-stream')   #opening and uploading the attachment
part.set_payload((attachment).read())  #read the attachment and set it as payload
encoders.encode_base64(part)    # encoding the email
part.add_header('Content-Disposition',"attachment; filename= "+filename) #adding the header for the e-mail
msg.attach(part)
# for file in files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_name = f.name
        
#         msg.add_attachment(file_data, maintype ='application', subtype = 'octet-stream', filename = file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    smtp.send_message(msg)    
