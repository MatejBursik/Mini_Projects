Triangle = [
[75],
[95,64],
[17,47,82],
[18,35,87,10],
[10,4,82,47,65]
]

path = []
Sums = []

for i in Triangle:
    Help = []
    Welp = []
    for j in i:
        Help.append("")
        Welp.append(0)
    path.append(Help)
    Sums.append(Welp)

Sums[0][0] = Triangle[0][0]
path[0][0] = str(Triangle[0][0])

for y,i in enumerate(Triangle):
    for x,i in enumerate(i):
        if y == (len(Triangle)-1):
            break

        if Sums[y+1][x] < Sums[y][x] + Triangle[y+1][x]:
            path[y+1][x] = str(path[y][x]) + "," + str(Triangle[y+1][x])
            Sums[y+1][x] = Sums[y][x] + Triangle[y+1][x]

        if Sums[y+1][x+1] < Sums[y][x] + Triangle[y+1][x+1]:
            path[y+1][x+1] = str(path[y][x]) + "," + str(Triangle[y+1][x+1])
            Sums[y+1][x+1] = Sums[y][x] + Triangle[y+1][x+1]

#print(path);    print(Sums)
MaxIndex = Sums[len(Sums)-1].index(max(Sums[len(Sums)-1]))
print(path[len(path)-1][MaxIndex], "is the path to get the highest outcome, which is",max(Sums[len(Sums)-1]))

