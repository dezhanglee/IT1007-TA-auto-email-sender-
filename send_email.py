import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(taskname, student_email, student_name, matric_no, filename, my_email, my_password):
    
    fromaddr = my_email
    toaddr = student_email
 
    msg = MIMEMultipart()
 
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Cc'] = fromaddr #cc a copy back to me 
    msg['Subject'] = "[IT1007] {} - {}".format(taskname, matric_no) #change subject as required 

    #change body as required, {} will auto insert the student's name as per the csv file
    body = "Hi {}, \n \nAttached is your graded {} with comments. \n \nPlease email me should you have any queries. \
                \n \nBest regards,\nDe Zhang".format(student_name, taskname)
 
    msg.attach(MIMEText(body, 'plain'))
 
    attachment = open(filename, "rb")
     
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    msg.attach(part)

    recipients = [toaddr, fromaddr] #add or remove recipients
    
    smtp = smtplib.SMTP('smtp.office365.com', 587) #for office365, change as required 
    smtp.ehlo()
    smtp.starttls()
    smtp.login(my_email, my_password)
    text = msg.as_string()
    smtp.sendmail(fromaddr, recipients, text)
    
    smtp.quit()
