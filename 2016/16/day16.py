input = "10001110011110000"

# demonstrating the power of xor

def curve(s):
    b = int(s[::-1], 2)^int("1"*len(s[::-1]), 2)
    return "{}0{:0{}b}".format(s,b,len(s))

def checksum(s):
    pairs = [s[x:x+2] for x in range(0, len(s), 2)]
    sum = []
    for pair in pairs:
        if pair[0] == pair[1]:
            sum.append("1")
        else:
            sum.append("0")
    if len(sum) % 2 == 0:
        sum = checksum("".join(sum))
    return "".join(sum)

disk = curve(input)
while len(disk) < 272:
    disk = curve(disk)

print checksum(disk[:272])