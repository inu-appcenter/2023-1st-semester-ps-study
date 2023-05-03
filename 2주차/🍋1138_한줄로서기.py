import sys

input=sys.stdin.readline

p=int(input())
a=list(map(int, input().split()))
r=[]

for i in range(0,p):
    r.append(0) #명수만큼 0을 추가

# 더 큰 사람 수만큼 빈자리를 건너뛰고 배치
for i in range(0,p): # i는 키 순으로 사람을 가르킴
    m=a[i] # i번째 사람이 건너뛰어야 할 인덱스 수, m이 0이 되면 r에 i를 추가
    n=0
    
    # r을 돌면서 빈칸인지 확인하는 반복문
    while True :
        if r[n]!=0: # n번째에 빈칸이 아닐경우
            n+=1 # 한칸 이동
        elif r[n]==0 and m>0: # 빈칸이고 큰 사람만큼 건너뛰지 않았으면
            m-=1 # 건너뛴 횟수를 셈
            n+=1 # 한칸 이동
        elif r[n]==0 and m==0: # 주어진만큼 건너뛰었지만 아직 자리를 못찾았을 때
            break

            
    r[n]=i+1
    
print(*r)
