a = int(input("Ведіть чотирьохзначне число: "))
suma=0
while a!=0:
    b = a%10
    suma=suma+b
    a=a//10
print(a,suma)