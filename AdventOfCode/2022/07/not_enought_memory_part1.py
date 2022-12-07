class Node:
    def __init__(self, index, parent=None, size=0):
        self.index = index
        self.parent = parent
        self.contents = {}
        self.size = size
        self.size_below = size


with open("AdventOfCode\\2022\\07\\input.txt") as f:
    data = f.readlines()
    arr = [i.replace("\n", "").split(" ") for i in data]

#tree making
root = Node(0)
index = 1
node_dict = {}
curr = root
for line in arr:
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                curr = curr.parent
            else:
                directory_name = line[2]
                if directory_name == "/":
                    curr = root
                else:
                    curr = curr.contents[directory_name]
    else:
        if line[0] == "dir":
            directory_name = line[1]
            node_dict[index] = Node(index, parent=curr)
            curr.contents[directory_name] = node_dict[index]
            index += 1
        else:
            size = int(line[0])
            file_name = line[1]
            node_dict[index] = Node(index, parent=curr, size=size)
            curr.contents[file_name] = node_dict[index]
            index += 1

#separating visited and not visited
answer = 0
to_visit = [root]
visited = set()
while len(to_visit) > 0:
    node = to_visit[-1]
    for sub in node.contents.values():
        if sub.index not in visited:
            to_visit.append(sub)
            break
    else:
        node = to_visit.pop()
        visited.add(node.index)
        if node.parent is not None:
            node.parent.size_below += node.size_below

        #identifying if their size is smaller or equal to 100000
        if (node.size_below <= 100000) and (len(node.contents) > 0):
            answer += node.size_below

print(answer)
