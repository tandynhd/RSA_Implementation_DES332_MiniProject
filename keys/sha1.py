import hashlib


#Check license
def check_license(Oneway_hash,digital_signature):
    # print(Oneway_hash,digital_signature)
    if Oneway_hash==digital_signature:
        print("Digital signature true")
    else:
        print("Digital signature not true")



#hash_object = hashlib.sha1(b'HelWorld')
#pbHash = hash_object.hexdigest()
#print(pbHash)
print("-------------------------------------------------------")
message=b'abc'
print("message = ",message)
print("-------------------------------------------------------")
h = hashlib.new("sha1",message)
sha1text = h.hexdigest()
sha1text = str(sha1text)
print("sha1 digest message = ",sha1text)
print("-------------------------------------------------------")
c=sha1text.encode()
print("encrypted sha1 digest message = ",c)
print("-------------------------------------------------------")
m=c.decode()
print("decrypted sha1 digest message = ",m)
print("-------------------------------------------------------")
check_license(sha1text,m)


