import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)

tree = {}
listing = False
name = ""
count = 0

with open("AdventOfCode\\2022\\07\\input.txt") as f:
    for line in f:
        line = line.strip().split(" ")

        if line[1] == "cd": #identifying change
            listing = False
            name = line[2]
            if (name not in tree.keys()) and (name != ".."):
                tree[name] = []

        elif line[1] == "ls": #identifying listing
            listing = True

        elif listing:
            if line[0].isdigit(): #identifying files and inner directories
                tree[name] += [int(line[0])]
            else:
                tree[name] += [line[1]]


def counting(_directory): #backpaddling recurssion through the "tree"
    global tree, count
    total = 0
    for i in tree[_directory]:
        if not str(i).isdigit():
            tree[i] = counting(i)
            total += tree[i]
        else:
            total += i
    count += 1
    print(count)
    return total

for i in tree:
    print(i,tree[i])

tree["root"] = counting("root")
print(tree)
