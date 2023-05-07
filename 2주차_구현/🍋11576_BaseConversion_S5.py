import sys

input=sys.stdin.readline

a, b=map(int, input().split())
c=int(input())
n=list(map(int, input().split()))

r=0#10진법으로 변환
for i in n:
    c-=1
    r+=i*(a**c)

result=[]
while r!=0:
    result.append(r%b)
    r=r//b
#print(r)
result.reverse()
print(*result)
