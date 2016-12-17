from collections import defaultdict

input = [x.split(" ") for x in open('input.txt').read().split("\n")]

dict = defaultdict(list)

for line in input:
    dict[int(line[1][1:])] = [int(line[3]), int(line[-1][:-1])]

dict[7] = [11, 0]
print dict

time = 0

while True:
    positions = []
    for i, pos in dict.iteritems():
        curr = (time + i + pos[1]) % pos[0]
        positions.append(curr)

    if all(x==0 for x in positions):
        print time
        break
    time += 1