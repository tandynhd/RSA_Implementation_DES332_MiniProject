import time
start = time.time()
from authentication import *
from confidentiality import *
# from flaskFE import data

def main(data):
    sender, receiver, message = data
    #Authentication
    sent = sendS(sender)
    print(sent)
    if sent == True:
        #Confidentiality
        email = sendM(message)
        print(email)
        end = time.time()
        total_time = end - start
        print("\n"+ str(total_time),"Seconds")



data = ("tandinhd@icloud.com", "hong@gmail.com", "How are you?")
main(data)


