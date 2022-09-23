import math
x=float(input("Ведіть x: "))
y=float(input("Ведіть y: "))
R1=math.sqrt(math.pow(100,2)+math.pow(64,2))
R2=math.sqrt(math.pow(10,2)+math.pow(8,2))
if x<=R1 and x>=R2 and y>=R2 and y<=R1:
    print("Точка координати належить кільцю")
else:
    print("Точка координати неналежить кільцю")
print(R1,R2)