from gui_generator import *

def Average(n):
    s = 0
    for x in range(n):
        s += int(g.addInput("Enter a value:"))
    return s / n

g = GUIgenerator()
g.create(Average, args=["How many numbers:"], desc="Calculate the average value.")
