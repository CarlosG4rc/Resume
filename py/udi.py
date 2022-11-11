import math

def areaCirculo(radio):
    return (radio**2) * math.pi

r = 2
r = int(r)
a = areaCirculo(r)
print("{:.4f}".format(a))