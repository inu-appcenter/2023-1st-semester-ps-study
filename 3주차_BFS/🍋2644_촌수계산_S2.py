import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
r1, r2=map(int, input().split())
m=int(input())
arr=[[]for _ in range(n+1)]


for i in range(m):
    a, b=map(int, input().split())
    arr[a].append(b)
    #arr[b].append(a)
print("arr:",arr)

def find(v1,v2): 
    r=0
    r+=1 #인풋으로 부모가 들어와서 하나 더함
    d=0
    while v1!=v2:
        d+=1
        r+=1
        for i in range(len(arr)):
            if v1 in arr[i]:
                v1=i    #자식으로 있으면 그 부모를 v1에 저장
        #print("r{} v1{} v2{}".format(r,v1,v2))
        if d>n:
            r = -2
            break
    r+=1
    return r
v=0
vv=0
for i in range(len(arr)):
    if r1 in arr[i]:
        v=i
    if r2 in arr[i]:
        vv=i
if v>vv:
    r=find(vv,v)
else:
    r=find(v,vv)
print("v{} vv{}".format(v,vv))
r=find(v,vv)
print(r)
#print("arr:",arr)

