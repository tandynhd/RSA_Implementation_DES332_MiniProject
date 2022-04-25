from pickle import SHORT_BINSTRING
from strBin import *
from math import *
from moduloExponentiation import *

# Purpose: break down a bit sequence into plain blocks, padding OneAndZeroes
def bitSeq2PlainBlocks(bitSeq):
       # padding OneAndZeroes 10...00, where the number 0 is plainBlockSize - len(bitSeq)%plainBlockSize
       bitSeq = bitSeq + "1" # always padding 1
       plainBlockSize = 7
       if len(bitSeq)%plainBlockSize != 0:
              bitSeq = bitSeq + "0" * (plainBlockSize - len(bitSeq)%plainBlockSize)
       plainBlocks = []
       noOfblocks = int(len(bitSeq)/plainBlockSize)
       for i in range(0,noOfblocks):
             plainBlocks.append(bitSeq[i*plainBlockSize:(i+1)*plainBlockSize])
       return plainBlocks

# Purpose: Remove the padding OneAndZeroes from a bit sequence (use in decryption)
def removePadding(bitSeq):
       # padding is 10..00 at the end
       indexOfOne = len(bitSeq)-1
       while bitSeq[indexOfOne]=="0":
              indexOfOne = indexOfOne -1
       return bitSeq[0:indexOfOne]

# Convert plain blocks into number sequence
def blocks2numberSeq(blocks):
       numSeq = []
       for b in blocks:
              numSeq.append(int(b,2))
       return numSeq

# Convert number sequence into blocks.    

def numberSeq2Blocks(numSeq, bsize):
       blocks = []
       for num in numSeq:
              block = bin(num) # 11 ==> '0b1011'; 166 => '0b10100110'; 4 => '0b100'
              block = block[2:] # trip of 0b at begining: '0b1011'  ==> "1011"; '0b10100110' => 10100110
              if len(block)<bsize:
                     block = "0"*(bsize-len(block)) + block # add 0
              blocks.append(block)
       return blocks


# RSA encryption
def rsaEncrypt(key, plainBitSeq):
       (e,n) = key
       plainBlockSize = floor(log(n,2))
       cipherBlockSize =  plainBlockSize + 1
       plainBlocks = bitSeq2PlainBlocks(plainBitSeq)
       print("plainBlocks = ", plainBlocks)
       plainNumSeq = blocks2numberSeq(plainBlocks)
       print("plainNumSeq = ", plainNumSeq)
       # encryption
       cipherNumSeq = []
       for plainNum in plainNumSeq:
            #   cipherNum = plainNum**e % n
              cipherNum = effModuloExp(plainNum,e,n)
              cipherNumSeq.append(cipherNum)
       print("cipherNumSeq = ", cipherNumSeq)
       cipherBlocks = numberSeq2Blocks(cipherNumSeq,cipherBlockSize)
       print("cipherBlocks = ", cipherBlocks)
       cipherBitSeq = ""
       for b in cipherBlocks:
              cipherBitSeq = cipherBitSeq + b
       return cipherBitSeq


# RSA decryption
def rsaDecrypt(key, cipherBitSeq):
       (d,n) = key
       plainBlockSize = floor(log(n,2))
       cipherBlockSize =  plainBlockSize + 1
       cipherBlocks = []
       numOfCipherBlocks = floor(len(cipherBitSeq)/cipherBlockSize)
       for i in range(0,numOfCipherBlocks):
              cipherBlocks.append(cipherBitSeq[i*cipherBlockSize: (i+1)*cipherBlockSize])
              
       print("cipherBlocks = ", cipherBlocks)
       cipherNumSeq = blocks2numberSeq(cipherBlocks)
       print("cipherNumSeq = ", cipherNumSeq)
       # decryption
       plainNumSeq = []
       for cipherNum in cipherNumSeq:
            #   plainNum = cipherNum**d % n
              plainNum = effModuloExp(cipherNum,d,n)
              plainNumSeq.append(plainNum)
       print("plainNumSeq", plainNumSeq)
       plainBlocks = numberSeq2Blocks(plainNumSeq,plainBlockSize)
       print("plainBlocks", plainBlocks)
       plainBitSeq = ""
       for pb in plainBlocks:
              plainBitSeq = plainBitSeq + pb
       print(plainBitSeq)
       return removePadding(plainBitSeq)

#convert clear-text to binary
def clearTextBin(clearText):
    binText = strToBinStr(clearText)
    return binText

# test = clearTextBin("What is your name my name is tandin dorji.?")
# print(test)
# print("Encryption")
# cipher = rsaEncrypt((11, 221), test)
# print(cipher)

# print("Decryption")

# decryptedClearText = rsaDecrypt((35,221),cipher)
# print(decryptedClearText)
# print(binStrToStr(decryptedClearText))
