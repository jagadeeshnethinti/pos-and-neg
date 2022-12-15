n=int(input())
a=[]
b=[]
for i in range(n):
    r=int(input())
    if r>0:
      a.append(r)
    elif r<0:
        b.append(r)
print(a,b)