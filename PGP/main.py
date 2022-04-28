import time
from authentication import *
from confidentiality import *
# from flaskFE import data

def main(data):
    start = time.time()
    username, sender, receiver, message = data
    #Authentication
    sent = sendS(username)
    # print(sent)
    if sent == True:
        #Confidentiality
        email = sendM(message)
        print(email)
        end = time.time()
        total_time = end - start

        print("\n"+ "Total time taken =",str(total_time),"Seconds")



# data = ["tandinhd","tandinhd@icloud.com", "hong@gmail.com", "How are you?"]
# main(data)


