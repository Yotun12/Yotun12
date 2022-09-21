import math
x=float(input("Ведіть x: "))
y=float(input("Ведіть y: "))
a=float(input("Ведіть a: "))
Z=(math.pow(x,3)+a)*(y-math.log1p(math.fabs(y))-math.sin(a))+math.sqrt(math.pow((math.pow(x,3)+y),3))
print(Z) 