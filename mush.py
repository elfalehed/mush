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




def cod(): 
    dd = open("intro1.txt", "r") 
    ddd = dd.read() 
    print(ddd) 
    op = input("$  ") 
    if op == 1: 
        Dmd5() 
    



# where it all makes sense 
def main():
    logo = open("banner.txt", "r")
    intro = open("intro.txt","r") 
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
