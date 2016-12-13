input = [x.split(" ") for x in open("input.txt").read().split("\n")]

registers = {'a': 0, 'b':0, 'c':1, 'd':0}
pc = 0

while True:
    try:
        x = input[pc]
    except:
        break

    if x[0] == "cpy":
        if x[1].isalpha():
            registers[x[2]] = registers[x[1]]
        else:
            registers[x[2]] = int(x[1])
        pc+=1

    elif x[0] == "inc":
        registers[x[1]] += 1
        pc += 1
    elif x[0] == "dec":
        registers[x[1]] -= 1
        pc+=1
    elif x[0] == "jnz":
        if not x[1].isalpha():
            if int(x[1]) != 0:
                pc += int(x[2])
            else:
                pc += 1
        else:
            if registers[x[1]] != 0:
                pc += int(x[2])
            else:
                pc += 1

print registers['a']