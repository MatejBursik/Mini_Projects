from math import *

def Check(value):
    ft = True
    for i in range(2,int(sqrt(value))+1):
        if value % i == 0:
            ft = False
            break

    return ft
