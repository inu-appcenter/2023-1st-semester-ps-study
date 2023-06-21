import sys
input=sys.stdin.readline

n=int(input())

for i in range(n):
    e=0
    rev=0
    func=input().strip()
    m=int(input())
    nn=((input().strip()).lstrip("[")).rstrip("]")
    if m==0:
        print("error")
        continue
    num=list(map(int, nn.split(sep=",")))
    for j in func:
        if j =="R":
            rev+=1
        elif j=="D":
            if len(num)==0:
                print("error")
                e=1
                break
            else:
                if rev%2==0:
                    del num[0]
                else:
                    del num[-1]
    if e==1:
        continue
    else:
        if rev%2==0:
            print("[" + ",".join(list(map(str, num))) + "]")
        else:
            num.reverse()
            print("[" + ",".join(list(map(str, num))) + "]")
