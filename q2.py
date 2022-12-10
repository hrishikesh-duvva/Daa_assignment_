arr=list(map(str,input().split(",")))
dep=list(map(str,input().split(",")))
arr1=[]
dep1=[]
for i,j in zip(arr,dep):
    b=i.split(':')
    a=int(b[0])*60+int(b[1])
    d=j.split(':')
    c=int(d[0])*60+int(d[1])
    arr1.append(a)
    dep1.append(c)
new=[i for i in arr1]
new.extend(i for i in dep1)
new.sort()
t=1
for i in range(1,len(new)):
    m=1
    while new[i-1] in arr1 and new[i] in arr1:
        i+=1
        m+=1
    if m>=t:
        t=m
print(t)