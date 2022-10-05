import math
x=float(input("Ведіть x: "))
def f1(x1):
    a=x+math.pow(2,x-4)-math.sqrt(x)
    return(a)
def f2(x2):
    a=math.sin(2*x2)+math.log(math.fabs(x))
    return(a)
def f3(x3):
    a=math.cos(3*x)-1/x
    return(a)

y=0.0

if x>=0:
    y=f1(x)
elif -7.7<x<0:
    y=f2(x)
else:
    y=f3(x)

print(y)

    