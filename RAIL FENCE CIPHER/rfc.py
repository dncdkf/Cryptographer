 
x=raw_input("enter the plaintext")
key=int(raw_input("enter the key"))
mat=[['0' for i in range(len(x))]for j in range(key)]
print(mat)
row=0
col=0
flag=0
for z in x:
    if row>key-1:
        flag=1
        row=row-2
        print('key-1',row,col)
        mat[row][col]=z
        continue
    if row==0 and col!=0:
        flag=0
        row=row+1
        col=col+1
        print('rowcol',row,col)
        mat[row][col]=z
        row=row+1
        col=col+1
        continue
    if flag==1:
        row=row-1
        col=col+1
        print('flag1',row,col)
        mat[row][col]=z
    
    if flag==0:
        print('flag0',row,col)
        mat[row][col]=z
        row=row+1
        col=col+1
        
    
    
print(mat)
res=""
for i in range(key):
    for j in range(len(x)):
        if mat[i][j]!='0':
            res=res+mat[i][j]
print(res)
dmat=[['0' for i in range(len(res))]for j in range(key)]
tempkey=key
r=0
c=0
prevc=0
for ch in res:
    if c>=len(res):
        c=prevc+1
        prevc+=1
        r+=1
        if tempkey/2<1:
            tempkey=1
        else:
            tempkey=tempkey/2
        # print('if1',r,c)
        dmat[r][c]=ch
        c=c+tempkey+1
        continue
    else:
        # print(r,c)
        dmat[r][c]=ch
        c=c+tempkey+1
print(dmat,len(res))
dec=''
counter=0
i=0
while i<key and i>=0:
    for j in range(len(res)):
        if dmat[i][j]!='0':
            print(counter,dec)
            dec=dec+dmat[i][j]
            dmat[i][j]='0'
            counter+=1
            i=i+1
            break
    if i==key and counter!=len(res):
        flag=1
    if i==key and counter==len(res):
        break
print(dec)
