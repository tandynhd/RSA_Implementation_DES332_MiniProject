import time
start = time.time()
from authentication import *
from confidentiality import *



#Authentication
sent = sendS("tandinhd@icloud.com")
print(sent)
if sent == True:
    #Confidentiality
    email = sendM("Hi i am tandin, What aer you doing here hope you are good to do")
    print(email)
    end = time.time()
    total_time = end - start
    print("\n"+ str(total_time),"Seconds")






