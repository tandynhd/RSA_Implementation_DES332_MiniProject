from math import *
from utils.moduloExpon import *

# Purpose: break down a bit sequence into plain blocks, padding OneAndZeroes
# (string, integer) => list of strings

# Ex: bitSeq2PlainBlocks("1011000110101011", 7) => ['1011000', '1101010', '1110000']

def bitSeq2PlainBlocks(bitSeq,plainBlockSize):
       # padding OneAndZeroes 10...00, where the number 0 is plainBlockSize - len(bitSeq)%plainBlockSize
       bitSeq = bitSeq + "1" # always padding 1
       if len(bitSeq)%plainBlockSize != 0:
              bitSeq = bitSeq + "0" * (plainBlockSize - len(bitSeq)%plainBlockSize)
       plainBlocks = []
       noOfblocks = int(len(bitSeq)/plainBlockSize)
       for i in range(0,noOfblocks):
             plainBlocks.append(bitSeq[i*plainBlockSize:(i+1)*plainBlockSize])
       return plainBlocks


# Purpose: Remove the padding OneAndZeroes from a bit sequence (use in decryption)
# string => string
# EX: removePadding("101100011010101110000") => "1011000110101011" 

def removePadding(bitSeq):
       # padding is 10..00 at the end
       indexOfOne = len(bitSeq)-1
       while bitSeq[indexOfOne]=="0":
              indexOfOne = indexOfOne -1
       return bitSeq[0:indexOfOne]


# Convert plain blocks into number sequence
# EX: blocks2numberSeq(['1011000', '1101010', '1110000']) =>  [88, 106, 112]
def blocks2numberSeq(blocks):
       numSeq = []
       for b in blocks:
              numSeq.append(int(b,2))
       return numSeq


# Convert number sequence into blocks. 
# EX:   numberSeq2Blocks([88, 106, 112],7) ==> ['1011000', '1101010', '1110000']
#       numberSeq2Blocks([121, 6, 73],8) => ['01111001', '00000110', '01001001']
#      

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
# EX: rsaEncrypt((5, 221),"1000100110101011") ==> "001100101101001000111"
# rsaEncrypt((107,143),"110101011000100") ==> 010010000011011001001100

def rsaEncrypt(key, plainBitSeq):
       print("==========================================")
       print("RSA Encryption Under Process ")
       (e,n) = key
       plainBlockSize = floor(log(n,2))
       cipherBlockSize =  plainBlockSize + 1
       plainBlocks = bitSeq2PlainBlocks(plainBitSeq,plainBlockSize)
       print("plainBlocks = ", plainBlocks)
       plainNumSeq = blocks2numberSeq(plainBlocks)
       print("plainNumSeq = ", plainNumSeq)
       # encryption
       cipherNumSeq = []
       for plainNum in plainNumSeq:
              # cipherNum = plainNum**e % n
              cipherNum = effModuloExp(plainNum,e,n)
              cipherNumSeq.append(cipherNum)
       print("cipherNumSeq = ", cipherNumSeq)
       cipherBlocks = numberSeq2Blocks(cipherNumSeq,cipherBlockSize)
       print("cipherBlocks = ", cipherBlocks)
       cipherBitSeq = ""
       for b in cipherBlocks:
              cipherBitSeq = cipherBitSeq + b
       print("RSA Encryption Completed ")
       print("==========================================")
       return cipherBitSeq


# RSA decryption
# EX: rsaDecrypt((37,77),"100010100101110010100") ==> "1011000110101011"
#      rsaDecrypt((53,143),"")

# 010010000011011001001111

# rsaDecrypt((77,221),"110000000111100001111101") ==> 010010000011011001001100
def rsaDecrypt(key, cipherBitSeq):
       print("==========================================")
       print("RSA Decryption Under Process ")
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
              # plainNum = cipherNum**d % n
              plainNum = effModuloExp(cipherNum,d,n)
              plainNumSeq.append(plainNum)
       print("plainNumSeq", plainNumSeq)
       plainBlocks = numberSeq2Blocks(plainNumSeq,plainBlockSize)
       print("plainBlocks", plainBlocks)
       plainBitSeq = ""
       for pb in plainBlocks:
              plainBitSeq = plainBitSeq + pb
       print("RSA Decryption Completed ")
       print("==========================================")
       return removePadding(plainBitSeq)

