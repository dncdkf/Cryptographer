def mod(a):
    if a>0:
        return a
    else:
        return a*-1
def encrypt(p,a,b):
    c=""
    for ch in p:
        x=ord(ch)-97
        y=(a*x+b)%26
        c=c+chr(y+97)
    return c

def decrypt(c,a,b):
    d=""
    a_1=0
    for z in range(0,25):
        if a*z%26==1:
            a_1=z
    print(a_1)
        
    for ch in c:
        x=ord(ch)-97
        print((a_1*(mod(x-b)))%26)
        print("x=",x)
        if x>=20:
            d=d+chr(97+(a_1*(mod(x-b)))%26)
            # print(d)
        else:
            d=d+chr(26+97-(a_1*(mod(x-b)))%26)
    return d
while True:
    option=int(raw_input("Press 1 to Encrypt \nPress 2 to Decrypt \nPress 3 to EXIT\n"))
    if option==1:
        p=raw_input("Enter the text : ")
        a=int(raw_input("Enter the first key : "))
        b=int(raw_input("Enter the second key : "))
        print(encrypt(p,a,b))
        continue
    if option==2:
        c=raw_input("Enter Encrypted text : ")
        a=int(raw_input("Enter the first key : "))
        b=int(raw_input("Enter the second key : "))
        print(decrypt(c,a,b))
        continue
    if option==3:
        break
    else:
        print("Choose a valid option")
        continue


   
