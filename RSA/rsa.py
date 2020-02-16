from random import randint

p=int(raw_input("enter a prime number"))
q=int(raw_input("enter another prime number"))
n=p*q
phi=(p-1)*(q-1)
e=0
print(n,phi)
for i in range(2,phi):
    j=randint(2,phi-1)
    if n%j!=0:
        e=j
        break
        
for k in range(1,10):
    d=((k*phi)+1)
    if d%e==0:
        d=int(d/e)
    print("asda",d)

print('k=',k,'e=',e,'d=',d,'phi=',phi)
d=((2*phi)+1)/e
inp=int(raw_input("encr"))
c=pow(inp,e)%n
print(c)
res=pow(c,d)%n
print(res)

