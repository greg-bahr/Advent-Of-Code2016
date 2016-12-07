import string
from collections import Counter

input = [x.split("[") for x in open("input.txt").read().split("\n")]
input.pop()

num = 0

real_rooms = []

#part 1
for x in input:
    x[1] = x[1][:-1]
    x.append(int(x[0][-3:]))
    x[0] = x[0][:-3]
    x[0] = "".join(x[0].split("-"))

    counter = Counter(x[0]).most_common()
    sorted_name = sorted(counter, key= lambda z: (-z[1], z[0]))
    checksum = "".join([sorted_name[y][0] for y in range(5)])

    if checksum == x[1]:
        num += x[2]
        real_rooms.append(x)

print num


#part 2
def decrypt(key, message):
    decrypted = ""
    key = key%26
    for char in message:
        num = ord(char)
        num += key

        if num > ord('z'):
            num -= 26
        elif num < ord('a'):
            num += 26

        decrypted += chr(num)
    return decrypted

for room in real_rooms:
    name = decrypt(room[2], room[0])
    if "northpole" in name:
        print room[2]
