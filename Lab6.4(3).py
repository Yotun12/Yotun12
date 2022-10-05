import math
a=float(input("Значення:a"))
b=float(input("Значення:b"))
h=float(input("Значення:h"))
x=a
y=0.0
spisok=[]
for i in range (10):
    y=7-x*math.pow(math.e,2*x-1)+math.sqrt(math.fabs(x))
    y=round(y,4)
    spisok.append(y)
    print(i,'',x,'',y)
    x=x+h
    x=round(x,1)
    if x>b:
        break
print(spisok)