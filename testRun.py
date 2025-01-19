from GUIgenerator import *

def Average(n):
    s = 0
    for x in range(n):
        s += int(g.addInput())
    return s / n

g = GUIgenerator()
g.create(Average, args=["How many numbers:"])
