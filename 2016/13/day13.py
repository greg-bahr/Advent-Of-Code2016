import sys

input = 1362



def create_maze(input):
    maze = [[0 for x in range(60)] for y in range(60)]
    for i in range(60):
        for j in range(60):
            num = (j*j) + (3*j) + (2*j*i) + i + (i*i) + input
            if bin(num).count("1") % 2 == 0:
                maze[i][j] = 0
            else:
                maze[i][j] = 1
    return maze

maze = create_maze(input)

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 1:
            sys.stdout.write("#")
        else:
            sys.stdout.write(".")
    print "\n"

visited = set()
queue = []

queue.append((1,1,0))
visited.add((1,1))

nodes_checked = 0

while queue:
    x, y, steps = queue.pop(0)
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    for neighbor in neighbors:
        nodes_checked += 1
        if neighbor[0] < 0 or neighbor[1] < 0 or maze[neighbor[1]][neighbor[0]] == 1 or neighbor in visited:
             pass
        else:
            queue.append((neighbor[0],neighbor[1], steps+1))

    if (31, 39) in visited:
        print steps
        break

    """
    if steps > 50:
        print len(visited)
        break
    """

    visited.add((x,y))


print "Nodes Checked: {}".format(nodes_checked)