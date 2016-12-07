from collections import Counter

input = open("input.txt").read().split("\n")
input.pop()
input = zip(*input)

password = []
password2 = []

for line in input:
    c = Counter(line).most_common()
    password.append(c[0][0])
    password2.append(c[-1][0])

print "".join(password)
print "".join(password2)
