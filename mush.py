#! /usr/bin/env python3 

# intro Mush: A multiple hash generator. 
# basically doing encrypting & decrypting comes later 

# importing stuff  
import hashlib 
from hashlib import md5


def Dmd5():
    string = input("Enter the word/sentence you want to decrypt?\n") 
    result = hashlib.md5(string.encode())

    print("the Hexadecimal equivalent of hash is: ", end="") 
    print(result.hexdigest())




def fun(): 
    dd = open("promtps/intro1.txt", "r") 
    ddd = dd.read() 
    print(ddd) 
    op = input("$  ") 
    if op == 1: 
        Dmd5() 

def cod(): 
    zz = open("prompts/intro2.txt", "r") 
    zzz = zz.read()
    print(zzz) 
    ol = input("$  ") 
    if ol == 1: 
        Dmorse()
    elif ol == 2:
        Dbinary()
    



# where it all makes sense 
def main():
    logo = open("banner.txt", "r")
    intro = open("prompts/intro.txt","r") 
    bn = logo.read()
    intrO = intro.read() 
    print(bn)
    print(intrO) 
    pp = input("$  ") 
    if pp == 1 : 
        fun()
    else: 
        cod() 


if __name__=='__main__':main() 
