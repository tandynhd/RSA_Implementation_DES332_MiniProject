import time
from authentication import *
from confidentiality import *
from EmailSMTP import sendEmail
# from flaskFE import data

def main(data):
    start = time.time()
    Sender = keys()
    Receiver = keys()

    username, sender, password, receiver, message = data
    #Authentication
    sent,digitalSign = sendS(username,Sender)
    # print(sent)
    if sent == True:
        #Confidentiality
        email = sendM(message,digitalSign,Receiver)
        print(email)
        end = time.time()
        total_time = end - start
        print("\n"+ "Total time taken =",str(total_time),"Seconds")
        start = time.time()
        return(sendEmail(sender,receiver,email,password))
        



# data = ["tandinhd","", "","", "How are you? Test 2"]
# data = [username, sEmail, spassword, rEmail, message]
# main(data)


