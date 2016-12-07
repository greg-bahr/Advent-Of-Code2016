input = open("input.txt").read().split("\n")
input = [x.split() for x in input]
input.pop()
n = 0

for x in input:
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    if (a+b)>c and (b+c)>a and (a+c)>b:
        n += 1

print n
