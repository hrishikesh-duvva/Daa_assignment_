r,c=map(int,input().split())
a=[]
for _ in range(r):
    b=list(map(int,input().split(",")))
    a.extend(b)
a.sort()
print(a)
print(a[(r*c+1)//2-1])