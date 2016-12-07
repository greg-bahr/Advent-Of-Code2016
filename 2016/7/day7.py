import re

input = []

ips = 0
ips2 = 0

for line in open("input.txt").readlines():
    input.append(re.split(r'\[(\w+)\]', line.rstrip("\n")))
    print input[-1]

def hasABBA(x):
    for i in range(len(x)):
        if x[i:i+2][::-1] == x[i+2:i+4] and not x[i] == x[i+2]:
            return True
    return False

def hasABA(x):
    ABAs = []
    for i in range(len(x)):
        if i<len(x)-2:
            if x[i] == x[i+2] and not x[i] == x[i+1]:
                ABAs.append(x[i]+x[i+1]+x[i+2])
    return ABAs

for ip in input:
    nonbrackets = []
    brackets = []
    for string in ip:
        if ip.index(string)%2 == 0:
            nonbrackets.append(string + " ")
        else:
            brackets.append(string + " ")

    ips = ips+1 if hasABBA("".join(nonbrackets)) and not hasABBA("".join(brackets)) else ips

    aba = hasABA("".join(nonbrackets))
    bab = hasABA("".join(brackets))

    if aba and bab:
        for x in aba:
            if x[1]+x[0]+x[1] in bab:
                ips2 += 1
                break

print ips
print ips2