import random
import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)

#adding TLS security

server.starttls()

#get your app password of gmail ----as directed in the video

password='ulareqnangzgraih'
server.login('vacchesakshi@gmail.com',password)

#generate OTP using random.randint() function

otp=''.join([str(random.randint(0,9)) for i in range(4)])
msg='Hello, Your OTP is '+str(otp)
sender='vacchesakshi@gmail.com'  #write email id of sender
receiver='vacche0304' #write email of receiver

#sendi
server.sendmail('vacchesakshi@gmail.com','vacchesakshi@gmail.com',msg)
server.quit()