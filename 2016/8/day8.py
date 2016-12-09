import re
import numpy as np
import sys

screen = np.zeros([6, 50], dtype=int)

input = open("input.txt").read().split("\n")
input = [x.split(" ") for x in input]
input.pop()

for line in input:
	if line[0] == "rect":
		dimm = [int(x) for x in line[1].split("x")]
		screen[:dimm[1], :dimm[0]] = 1
	if line[0] == "rotate":
		if line[1] == "row":
			screen[int(line[2][2:])] = np.roll(screen[int(line[2][2:])], int(line[-1]))
		if line[1] == "column":
			screen.T[int(line[2][2:])] = np.roll(screen.T[int(line[2][2:])], int(line[-1]))


print screen.sum()

for i in range(len(screen)):
	for j in range(len(screen[i])):
		if screen[i,j] == 1:
			sys.stdout.write("X")
		else:
			sys.stdout.write("_")
	print "\n"
