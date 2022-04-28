import time
from authentication import *
from confidentiality import *
# from flaskFE import data

def main(data):
    start = time.time()
    Sender = keys()
    Receiver = keys()

    username, sender, receiver, message = data
    #Authentication
    sent,digitalSign = sendS(username)
    # print(sent)
    if sent == True:
        #Confidentiality
        email = sendM(message,digitalSign)
        print(email)
        end = time.time()
        total_time = end - start
        print("\n"+ "Total time taken =",str(total_time),"Seconds")
        start = time.time()



data = ["tandinhd","tandinhd@icloud.com", "hong@gmail.com", "How are you?"]
main(data)


