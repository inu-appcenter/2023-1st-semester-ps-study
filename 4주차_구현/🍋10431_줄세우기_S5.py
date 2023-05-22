import sys
input=sys.stdin.readline

n=int(input())
student=[[] for _ in range(n)]
r=[]

def fuc1(stu) :
    s=[]
    r1=0
    #student=list(map(int, input().split()))
    #print("함수안입니다",stu)
    stu=stu[1:]
    #print("왜일까요student{} s{}".format(stu, s))
    s.append(stu[0])
    for j in stu:
        #removec=0
        s1=reversed(s)
        for k in s1:
            #print("s{} r{} j{} k{} append".format(s,r1,j,k))
            if j<k:
                if j in s:
                    #if removec!=0:
                        #break
                    s.remove(j)
                    #removec+=1
                s.insert(s.index(k),j)
                r1+=1
                #print("s{} r{} j{} k{} insert".format(s,r1,j,k))
            elif j>k:
                if j in s:
                    s.remove(j)
                    #removec+=1
                    
                s.append(j)
                #print("s{} r{} j{} k{} append".format(s,r1,j,k))
    r.append(r1)
    #print(r)
    #o=input()
    return r

for i in range(n):
    student[i]=list(map(int, input().split()))

#fuc1(student[2])
for i in range(n):
    fuc1(student[i])
    print(i+1, r[i])
