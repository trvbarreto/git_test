import smtplib
from email.message import EmailMessage

email_address = 'trvb.test@gmail.com'
email_password = 'lpgvojojhnxkfenw'

email = EmailMessage()
email['from'] = 'Gran Torino'
email['to'] = 'trvb.test@gmail.com'
email['subject'] = 'You won 1.000.000 dollars!'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_address, email_password)
    smtp.send_message(email)
    print('all good boss!!')
