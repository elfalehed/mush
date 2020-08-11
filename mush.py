#! /usr/bin/env python3 

# importing stuff  
import hashlib 
from hashlib import md5


def md5():
    string = input("Enter the word/sentence you want to decrypt?\n") 
    result = hashlib.md5(string.encode())

    print("the Hexadecimal equivalent of hash is: ", end="") 
    print(result.hexdigest())





def main():

    md5() 

if __name__=='__main__':main() 
