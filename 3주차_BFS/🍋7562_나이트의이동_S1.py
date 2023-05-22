import sys
input=sys.stdin.readline

n=int(input())
move=[[-1,-2], [-1,2], [1,-2], [1,2], [-2,-1], [-2,1], [2,-1], [2,1]]
r=[]
for j in range(n):
    m=int(input())
    board=[[[0] for _ in range(m)] for _ in range(m)]
    print(board)
    s1,s2=map(int, input().split())
    status=[[s1,s2]for _ in range(3)] # 횟수카운트, start, finish
    visited=[]
    status[0]=0
    #board[s1][s2]=0
    f1,f2=map(int, input().split())
    status[2]=[f1,f2]
    print(status)
    #board[f1][f2]=99
    e=0
    visited.append([s1,s2])
    board[s1][s2]=[1]
    print("while들어가기전visited",visited)
    while visited:
        o=input()
        print("삭제전",visited)
        x=visited[len(visited)-1][0]
        y=visited[len(visited)-1][1]
        visited.remove([x,y])
        print("for들어가기전vis
              ited",visited)
        for i in range(8):
            nx=x+move[i][0]
            ny=y+move[i][1]
            print("연산은 잘 됐니 x{} y{}".format(nx,ny))
            if 0<=nx<=m-1 and 0<=ny<=m-1:
                print("board값 확인해볼까",board[nx][ny])
                if board[nx][ny]==[0]:
                    visited.append([nx,ny])
                    board[nx][ny]=[1]
                    print("잘 들어갔니 x{} y{} visited{}".format(nx,ny,visited))
                if i==7:
                    status[0]=status[0]+1
                #print("status{} i{}".format(status,i))
                print("도착지",status[2][0])
                if nx==status[2][0] and ny==status[2][1]:
                    visited=[]
                    break
    print("종료",status)
    #print(board)
