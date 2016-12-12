import re
from collections import defaultdict

input = [x.split(" ") for x in open("input.txt").read().strip().split("\n")]

bots = defaultdict(list)
output = defaultdict(list)

for line in input:
    if "value" in line:
        bots[line[-1]].append(int(line[1]))

def done(bot):
    for k, v in bot.iteritems():
        if len(v) == 2:
            return False
    return True

while not done(bots):
    for line in input:
        if line[0] == "bot" and len(bots[line[1]]) == 2:
            id, low, high = re.findall(r'\d+', " ".join(line))
            if bots[id] == [61, 17]:
                print id

            if line[5] == "output":
                output[low].append(min(bots[id]))
            else:
                bots[low].append(min(bots[id]))

            if line[10] == "output":
                output[high].append(max(bots[id]))
            else:
                bots[high].append(max(bots[id]))
            bots.pop(id)

print output["0"][0] * output["1"][0] * output["2"][0] # wtf is this