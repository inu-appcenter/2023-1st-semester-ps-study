import sys
input=sys.stdin.readline

m=input().strip()
mm=[]
for i in m:
    if i =="+" or i=="-":
        mm.append(i)
    else:
        if len(mm)==0:
            mm.append(i)
        elif mm[len(mm)-1]!="+" and mm[len(mm)-1]!="-":
            mm.append(mm.pop()+i)
        else:
            mm.append(i)
r=[]

while mm:
    if "-" in mm:
        for _ in range(mm.count("-")):
            nn=[]
            ind=mm.index("-")#첫-
            mm.remove("-")
            if "-" in mm: #다음 - 있으면 그 사이까지 다 더해서 음수로 만듦
                for i in mm[ind:mm.index("-")]:
                    if i =="+":
                        mm.remove(i)
                    else:
                        nn.append(int(i))
                        mm.remove(i)
            else: #이 뒤로 -또 없으면
                for i in mm[ind:]:#-뒤에 모든 숫자 더함
                    if i =="+":
                        mm.remove(i)
                    else:
                        nn.append(int(i))
                        mm.remove(i)
            #n=int("-"+mm[mm.index("-")+1]) #-가 있으면 음수로 괄호치고 기존 리스트에서 삭제
            n=int(-(sum(nn)))
            #del mm[mm.index("-")+1]
            r.append(n)
    else:
        for i in mm:
            if i =="+":
                mm.remove(i)
            else:
                r.append(int(i))
                mm.remove(i)
print(sum(r))
