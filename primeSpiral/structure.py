import primeCheck

size = int(input("size of spiral (only odd size): "))
spiral = [];    field = []
number = size*size

for i in range(1,number+1):
    field.append([i,primeCheck.Check(i)])
field[0][1] = False

for i in range(size):
    block = []
    for k in range(size):
        block.append(" ")
    spiral.append(block)

pos = [size//2,size//2]

run = []
for i in range(size-1):
    run.append(i+1)    
    run.append(i+1)  
run.append(run[len(run)-1])

format = ["r","u","l","d"]; directions = []
for i in range(size//2):
    for k in format:
        directions.append(k)
directions.append("r")


print(field)
print(run)
print(directions)
#r=+x; u=-y; l=-x; d=+y
count = 0 #counting position in field
spiral[pos[1]][pos[0]] = "X" if field[count][1]==True else "O"
count += 1

for i,dirct in enumerate(directions):
    for l in range(run[i]):
        if dirct == "r":
            pos[0] += 1
        elif dirct == "u":
            pos[1] -= 1
        elif dirct == "l":
            pos[0] -= 1
        elif dirct == "d":
            pos[1] += 1

        spiral[pos[1]][pos[0]] = "X" if field[count][1]==True else "O"
        count+=1

print(spiral)