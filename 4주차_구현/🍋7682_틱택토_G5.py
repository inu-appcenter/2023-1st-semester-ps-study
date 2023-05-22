import sys
input=sys.stdin.readline

def isline(ttt, ox):
    #3줄이 만들어진 경우
    
    #가로
    if ttt[0]==ttt[1]==ttt[2]==ox:
        return True
    elif ttt[3]==ttt[4]==ttt[5]==ox:
        return True
    elif ttt[6]==ttt[7]==ttt[8]==ox:
        return True
    #세로
    elif ttt[0]==ttt[3]==ttt[6]==ox:
        return True
    elif ttt[1]==ttt[4]==ttt[7]==ox:
        return True
    elif ttt[2]==ttt[5]==ttt[8]==ox:
        return True
    #대각선
    elif ttt[0]==ttt[4]==ttt[8]==ox:
        return True
    elif ttt[2]==ttt[4]==ttt[6]==ox:
        return True
    return False


while True:
    ttt=input().strip()
    if ttt=="end":
        break

    winx, wino=isline(ttt, "X"),isline(ttt, "O")
    numx, numo=ttt.count("X"),ttt.count("O")
    
    #x가 이기는 경우
    if winx and not wino and numx == numo + 1:
        print("valid")
    #O가 이기는 경우
    elif not winx and wino and numx == numo:
        print("valid")
    #모든칸이 다 찼을 경우, 비기는 경우 
    elif not winx and not wino and numx == 5 and numo == 4:
        print("valid")
    else:
        print("invalid")
