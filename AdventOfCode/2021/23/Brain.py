map = [
["-","-","-","-","-","-","-","-","-","-","-","-","-"],
["-"," "," "," "," "," "," "," "," "," "," "," ","-"],
["-","-","-"," ","-"," ","-"," ","-"," ","-","-","-"],
["-","-","-"," ","-"," ","-"," ","-"," ","-","-","-"],
["-","-","-"," ","-"," ","-"," ","-"," ","-","-","-"],
["-","-","-"," ","-"," ","-"," ","-"," ","-","-","-"],
["-","-","-","-","-","-","-","-","-","-","-","-","-"]]

final = [
["-","-","-","-","-","-","-","-","-","-","-","-","-"],
["-"," "," "," "," "," "," "," "," "," "," "," ","-"],
["-","-","-","A","-","B","-","C","-","D","-","-","-"],
["-","-","-","A","-","B","-","C","-","D","-","-","-"],
["-","-","-","A","-","B","-","C","-","D","-","-","-"],
["-","-","-","A","-","B","-","C","-","D","-","-","-"],
["-","-","-","-","-","-","-","-","-","-","-","-","-"]]

letters = {"A":0,"B":0,"C":0,"D":0}

def move():
    for line in map:
        for space in line:
            if space in letters:
                pass



while map != final:
    pass



print(map)