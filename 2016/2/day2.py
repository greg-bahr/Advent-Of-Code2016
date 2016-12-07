input = open("input.txt").read().split("\n")

code = []

keypad = [[1], [2,3,4], [5,6,7,8,9], ["A", "B", "C"], ["D"]]

curr_button = 5

for num in input:
	print len(num)
	for letter in num:
		if letter == "U":
			curr_button = curr_button-3 if curr_button - 3 >= 0 else curr_button
		elif letter == "D":
			curr_button = curr_button+3 if curr_button + 3 <= 9 else curr_button
		elif letter == "R":
			curr_button = curr_button+1 if (curr_button)%3 != 0 else curr_button
		elif letter == "L":
			curr_button = curr_button-1 if (curr_button)%3 != 1 else curr_button
		print "Setting curr_button to {}".format(curr_button)
	code.append(curr_button)

print code
print len(input)
