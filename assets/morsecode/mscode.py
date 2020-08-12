#! /usr/bin/env python3 

import alphabet 
from alphabet import LATIN

ss = input("ENTER A TEXT/WORD YOU WANNA DECRYPT:  ") 
result = "" 
for vv in LATIN.values(): 
    for w in ss: 
           if w.upper() in dict: 
                result = result + LATIN[w] 
    
print(result) 
