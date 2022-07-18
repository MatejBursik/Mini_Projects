import time

def get_GMT_0():
    num = time.gmtime(time.time())
    txt = time.asctime(num)
    return(txt)

def get_GMT_local():
    num = time.localtime(time.time())
    txt = time.asctime(num)
    return(txt)