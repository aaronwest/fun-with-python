__author__ = "Aaron S. West"

def F():
    #print "F start"
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

def SubFib(startNumber, endNumber):
    for cur in F():
        #print "SubFib " + str(cur)
        if cur > endNumber: return
        if cur >= startNumber:
            yield cur

for i in SubFib(0, 50):
    print i
