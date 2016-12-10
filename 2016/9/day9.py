import re

input = open("input.txt").read()[:-1]

def decompress(string, recur):
    length = 0

    while "(" in string:
        length += string.index("(")
        string = string[string.index("("):]
        instr = [int(x) for x in re.findall(r'[0-9]+', string[:string.index(")")])]
        string = string[string.index(")")+1:]
        if recur:
            length += decompress(string[:instr[0]], True)*instr[1]
        else:
            length += instr[0]*instr[1]
        string = string[instr[0]:]
    length += len(string)
    return length

print decompress(input, False)
print decompress(input, True)