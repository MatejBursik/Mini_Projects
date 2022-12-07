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

#getting total size
total_used = root.size_below
total_free = 70000000 - total_used
amount_to_delete = 30000000 - total_free

#finding the smallest directory to delete
answer = root.size_below
for index, node in node_dict.items():
    if (len(node.contents) > 0) and (node.size_below < answer) and (node.size_below >= amount_to_delete):
        answer = node.size_below

print(answer)
