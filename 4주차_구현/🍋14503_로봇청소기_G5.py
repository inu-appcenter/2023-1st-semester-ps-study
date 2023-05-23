import sys
input=sys.stdin.readline

n,m=map(int, input().split())
r,c,d=map(int, input().split()) #0북 1동 2남 3서
room=[[]for _ in range(n)]
cleancount=0
for i in range(n):
    room[i]=list(map(int, input().split()))
#print("시작 맵")
#print(room)
def checkrange(rc, cc):
    if 0<=rc<=n-1 and 0<=cc<=m-1:
        return True
    else:
        return False

def foursides(rf,cf):
    rt=[0,0,0,0]
    if checkrange(rf,cf):
        if room[rf-1][cf]==0:
            rt[0]=1
        if room[rf+1][cf]==0:
            rt[2]=1
        if room[rf][cf-1]==0:
            rt[3]=1
        if room[rf][cf+1]==0:
            rt[1]=1
        return rt

def clean(r,c):
    while True:
        #print(room)
        #print("이번while의 상태 r{} c{} room[r][c]{}".format(r,c,room[r][c]))
        #o=input()
        if checkrange(r,c) and room[r][c]==0:
            room[r][c]=2 #청소
            global cleancount
            cleancount+=1
            #print("청소했는가 cleanout{} room[r][c]{}".format(cleancount, room[r][c]))
        if 1 in foursides(r,c):
            #print("3번들어가는 if문")
            global d
            for i in range(4):
                if d==0:
                    d=3
                else:
                    d-=1 #반시계회전 0321
                rt=foursides(r,c)
                #print("전진for문안 i{} d{} rt{}".format(i, d, rt))
                if rt[d]==1:
                    if d==0:    #보는방향으로전진
                        if checkrange(r-1, c):
                            r=r-1
                            break
                    elif d==1:
                        if checkrange(r, c+1):
                            c=c+1
                            break
                    elif d==2:
                        if checkrange(r+1, c):
                            r=r+1
                            break
                    elif d==3:
                        if checkrange(r, c-1):
                            c=c-1
                            break
                                        
            continue    #1번으로 돌아감
        else:
            #print("청소된빈칸이 없는 2번 else문")
            #if checkrange(r,c): #벽이 아니면, 후진 가능하면
            if d==0 and room[r+1][c]!=1:    #보는방향으로후진
                if checkrange(r+1, c):
                    r=r+1
            elif d==1 and room[r][c-1]!=1:
                if checkrange(r, c-1):
                    c=c-1
            elif d==2 and room[r-1][c]!=1:
                if checkrange(r-1, c):
                    r=r-1
            elif d==3 and room[r][c+1]!=1:
                if checkrange(r, c+1):
                    c=c+1
            else:
                break #종료
            continue #1로돌아감
clean(r,c)
print(cleancount)
