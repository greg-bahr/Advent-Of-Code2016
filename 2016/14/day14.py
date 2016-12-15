import hashlib
from collections import defaultdict

input = "ngcjuoqr"

key = 0
index = 0
table = defaultdict()


def stretch(s):
    for l in range(2017):
        s = hashlib.md5(s).hexdigest()
    return s

def check_next(i, char):
    for y in range(i+1,i+1001):
        if y in table:
            md5 = table[y]
        else:
            md5 = stretch(input+str(y))
            table[y] = md5
        for x in range(len(md5)-4):
            if char*5 == md5[x:x+5]:
                print "MD5: "+md5
                return True

""" probably should use regex to do this but im too lazy """

while key < 64:
    if index in table:
        hash = table[index]
    else:
        hash = stretch(input+str(index))
    index += 1
    for x in range(len(hash)-2):
        if hash[x]*3 == hash[x:x+3]:
           if check_next(index, hash[x]):
               print "Hash: "+hash
               key+=1
           break

print index-1