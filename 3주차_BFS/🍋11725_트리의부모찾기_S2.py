import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
arr=[[]for _ in range(n+1)]
r=[0,0]

for i in range(n-1):
    a, b=map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    r.append(0)

def find(v):
    
    for i in arr[v]:
        r[i]=v
        if v in arr[i]:
            arr[i].remove(v)
        if len(arr[i])>0:
            find(i)

find(1)
r[1]=0
r=r[2:]
#print("arr:",arr)
for i in r:
    print(i)
