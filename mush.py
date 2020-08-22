#! /usr/bin/env python3 
# utf-8 
'''
 / / Thanks to my @0xrick for the refreshing ideas  
/ / Greetz to @v1s1t0r the creator of @Airgeddo for contacting Me. 
'''

# importing Hashs  
import hashlib 
import os, sys
from os import system, name
import subprocess 
from hashlib import md5
from zlib import *
import socket 
import random 
import glob 
import base64 
import getpass
import colorama
from colorama import * 
from sys import argv
from time import gmtime, strftime, sleep
colorama.init()

HEADER = '\033[95m'
IMPORTANT = '\33[35m'
NOTICE = '\033[33m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
RED = '\033[91m'
END = '\033[0m'
UNDERLINE = '\033[4m'
LOGGING = '\33[34m'

color_random=[HEADER,IMPORTANT,NOTICE,OKBLUE,OKGREEN,WARNING,RED,END,UNDERLINE,LOGGING]
random.shuffle(color_random)
mushlogo = color_random[0] + '''
           __  _____  _______ 
   / |  / / / / / ___// / / /
  / /|_/ / / / /\__ \/ /_/ / 
 / /  / / /_/ /___/ / __  /  
/_/  /_/\____//____/_/ /_/         
'''

mushprompt = "mush ~# "
class mush:

    def choice(self):
        choice = input(mushprompt) 
        if choice == "1": 
            self.Dmd5()
        elif choice == "2": 
            self.dec()
        elif choice == "3": 
            self.enc() 
        elif choice == "4": 
            self.about() 
        else:
            print(RED + "       WRONG ANSWER!!! \n")
            print() 
            mush()

    # Hashing using md5 
    def Dmd5(self):
        string = input("Enter the word/sentence you want to decrypt?\n") 
        result = hashlib.md5(string.encode())

        print("the Hexadecimal equivalent of hash is: ", end="") 
        print(result.hexdigest())
        self.choice()

    def dec(self):
        pass

    def enc(self):
        pass

    def about(self):
        pass

    def run(self):
        print(mushlogo + RED + ''' 
        [*] The Quiter You Become, The More You Are Able To Hear! 
        [!] Mush is a multiple hashing/encrypting tool. ENJOY hashing/encrypting things! 
        ''' + END +'''
        {1} -- HASHING 
        {2} -- ENCRYPTING
        {3} -- DECRYPTING 
        {4} -- ABOUT  \n


        ''')
        self.choice()
            

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
        Emorse()
    elif ol == 2:
        Ebinary()

   
if __name__=='__main__': 
       try:
          os.system('cls' if os.name=='nt' else 'clear')
          mushObject= mush()
          mushObject.run()
       except KeyboardInterrupt: 
           print(" SOMETHIGN WRONG! ...\n") 
           time.sleep(0.25) 
