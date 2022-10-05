import math
a=float(input("Значення:a"))
b=float(input("Значення:b"))
h=float(input("Значення:h"))
x=a
y=0.0
for i in range (10):
    y=7-x*math.pow(math.e,2*x-1)+math.sqrt(math.fabs(x))
    print("x=%.1f y=%.3f" %(x,y))
    x=x+h
