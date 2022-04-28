import smtplib

def sendEmail(sentBy,receivedBy,mail,senderPassword):
    if sentBy == "":
        sender_email = "ktp.des332work@gmail.com"  # Email account of sender
        password = "ktp.1234"
    else:
        sender_email = sentBy
        password = senderPassword

    if receivedBy == "":
        receiver_email = "hackdorji@gmail.com"  # Email account of sender
        # receiver_email = "hung.nd.siit@gmail.com"  # Email account of receiver
    else:
        receiver_email = receivedBy

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()
    # Authentication
    s.login(sender_email, password)
    # message to be sent
    if mail == "":
        message = "Hello! This is KTP, send an email securely using our services."
    else:
        message = mail
    # sending the mail
    s.sendmail(sender_email, receiver_email, message)
    # terminating the session
    s.quit()

# sendEmail("","","","")