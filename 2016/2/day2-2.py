input = open("input.txt").read().split("\n")

code = []

keypad = [[2,3,4], [5,6,7,8,9], ["A", "B", "C"]]

curr_button = 5

for num in input:
	print len(num)
	for letter in num:
		if letter == "U":
			if curr_button in keypad[1]:
				if curr_button == 6 or curr_button == 7 or curr_button == 8:
					curr_button-=4
			elif curr_button in keypad[0]:
				if curr_button == 3:
					curr_button -= 2
			elif curr_button in keypad[2]:
				if curr_button == "B":
					curr_button = 7
				elif curr_button == "A":
					curr_button = 6
				elif curr_button == "C":
					curr_button = 8
			elif curr_button == "D":
				curr_button = "B"

		elif letter == "D":
			if curr_button in keypad[1]:
				if curr_button == 6:
					curr_button = "A"
				elif curr_button == 7:
					curr_button = "B"
				elif curr_button == 8:
					curr_button = "C"
			elif curr_button in keypad[0]:
				curr_button +=4
			elif curr_button in keypad[2]:
				if curr_button == "B":
					curr_button = "D"
			elif curr_button == 1:
				curr_button += 2
		elif letter == "R":
			for list in keypad:
				if curr_button in list:
					if type(curr_button) is str:
						curr_button = list[list.index(curr_button)+1] if curr_button != "C" else curr_button
					else:
						curr_button = curr_button+1 if curr_button<list[-1] else curr_button
		elif letter == "L":
			for list in keypad:
				if curr_button in list:
					if type(curr_button) is str:
						curr_button = list[list.index(curr_button)-1] if curr_button != "A" else curr_button
					else:
						curr_button = curr_button-1 if curr_button>list[0] else curr_button

	code.append(curr_button)

print code
print len(input)
