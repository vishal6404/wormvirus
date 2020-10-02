'''Worm mail'''
import smtplib
email=input("ENTER ANY EMAIL ID: ")
for i in range(1,21):
    server=smtplib.SMTP("smtp.gmail.com","587") # Smtp deatils & port
    server.starttls()
    server.login("coolv926@gmail.com","useyourpasswordandid") # use your app generated password or your password
    message="Your mail has been affected by worm virus ;) tc"#input("your message:- ")
    n=25#int(input("No. of time wanna send msg.:- ")) # no. of messsages to be sent in a loop
 
    for i in range(1,n+1):
        server.sendmail("coolv926@gmail.com",email,message)
    for i in range(1,n+1):
        server.sendmail("coolv926@gmail.com",email,message)
    server.quit()
print(":) succesfully sent 1000 worms")
