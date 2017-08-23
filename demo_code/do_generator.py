def triangles():
    L1=[1]
    while 1:
        yield L1
        L=L1
        a = 0
        while a<len(L):
            if a==0:L1=[1]
            else:L1.append(L[a-1]+L[a])
            a=a+1
        L1.append(1)
x = 0
for t in triangles():
    print(t)
    x= x + 1
    if x == 10:
        break
