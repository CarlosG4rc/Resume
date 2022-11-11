import math

def areaCirculo(radio):
    return (radio**2) * math.pi

r = input ("Cuál es el radio del circulo? " )
r = int(r)
a = areaCirculo(r)
print("{:.4f}".format(a))