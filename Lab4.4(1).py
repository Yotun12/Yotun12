import math
def func02(x1):
    y=math.cos(math.fabs(math.pow(x1,3)-math.pow(4,3)))+ math.log1p(math.fabs(x1))/math.sqrt(math.pow(x1-8+math.pow(x1,2),3))
    return(y)
x=float(input("Ведіть x"))
y=func02(x)
print(y) 