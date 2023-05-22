import sys
input=sys.stdin.readline

a,b,c=map(int, input().split())
s1, e1=map(int, input().split())
s2, e2=map(int, input().split())
s3, e3=map(int, input().split())
start=min(s1,s2,s3)
end=max(e1,e2,e3)
r=0
for i in range(start, end+1):
    m=0
    if s1<=i<e1:
        m+=1
    if s2<=i<e2:
        m+=1
    if s3<=i<e3:
        m+=1
    if m==1:
        r+=a
    elif m==2:
        r+=b*2
    elif m==3:
        r+=c*3

print(r)
