import math

def padding(a):
  pads=8-len(a)
  pm=''
  for i in range (pads):
    pm+='0'
  return pm

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    bins = str((bin(i)[2:]))
    pbin = padding(bins)+bins
    m.append((pbin))
  return m

def toBinaryStr(binary):
    string = ''.join([str(item) for item in binary])
    return string

def bstoBinary(a_string):
  split_strings = []
  n  = 8
  for index in range(0, len(a_string), n):
      split_strings.append(int(a_string[index : index + n]))

  return (split_strings)

def toString(a):
  l=[]
  m=""
  # a = int(a)
  for i in a:
    b=0
    c=0
    k=int(math.log10(i))+1
    for j in range(k):
      b=((i%10)*(2**j))   
      i=i//10
      c=c+b
    l.append(c)
  for x in l:
    m=m+chr(x)
  return m

def strToBinStr(string):
    binary = toBinary(string)
    print(binary)
    binaryString = toBinaryStr(binary)
    return (binaryString)

def binStrToStr(binStr):
  binary = bstoBinary(binStr)
  string = toString(binary)
  return string




# test = strToBinStr("Hello how are you? I am fine.")
# print(test)
# # test2 = binStrToStr(test)
# # print(test2)

# binary = bstoBinary(test)
# print(binary)
# string = toString(binary)
# print(string)

