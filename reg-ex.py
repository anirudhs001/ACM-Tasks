import re

#take in the input 
inp = input()

#split in words
LIST = re.split(" ", inp)

#check all words:
for x in LIST:
    #if it begins with vowel and ends without it
    temp = re.findall("^[aeiou].*[^aeiou]$", x)
    
    #if yes, print it
    if len(temp):
        print(temp)