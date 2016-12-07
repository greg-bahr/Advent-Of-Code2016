input = [map(int, x.split()) for x in open("input.txt").read().split("\n")]
input.pop()

n = 0

for i in range(len(input)/3):
    for x in range(3):
        a = input[(i*3)][x]
        b = input[(i*3)+1][x]
        c = input[(i*3)+2][x]

        if (a+b)>c and (b+c)>a and (a+c)>b:
            n += 1

print n
