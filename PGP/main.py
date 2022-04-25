from authentication import *
from confidentiality import *

#Authentication
sent = sendS("tandinhd@icloud.com")
print(sent)
if sent == True:
    print(1)
    #Confidentiality
    email = sendM("Hi i am tandin, What aer you doing here hope you are good to do")
    print(email)






