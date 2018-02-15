from send_email import *

from csv_dict import *

import glob

my_email = '' #input your email login id
my_password = '' #input your email password

students = {}
students = read_csv("matric_name_email.csv") #get dict with matric no as key, [name, email] as item

skipped_filenames = [] #files you dont want to send

directory_name='' #leave blank if same directory

unable_to_send = []

for fname in glob.glob(directory_name+'*.py'):
    
    if (fname in skipped_filenames): #skip specific files
        continue
    
    matric_no=fname[14:23] #Assuming student adheres to file naming format

    if (matric_no not in students): #if student names file wrongly or not in my group
        unable_to_send.append((fname, matric_no))
        continue
    
    student_email=students[matric_no][1]
    student_name=students[matric_no][0]

    send_email(student_email, student_name, fname, my_email, my_password)
    
#print list of emails not able to send for manual action
print("Unable to send the following files with their corresponding matric no:")

for item in unable_to_send:
    print(item)

