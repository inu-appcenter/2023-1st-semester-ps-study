import sys

input=sys.stdin.readline

a=list(input())
r=[]
n=0
for i in range(0,len(a)):
    r.append(0) #a길이만큼 공백을 추가

while n<len(a):
    alpha=[]
    if ord(a[n])==60: # < 만나면
        while True:             # > 만날때까지 반복
            if ord(a[n])==62:
                break
            r[n]=a[n]
            n+=1            # r에 a그대로 옮기고 인덱스+1

    elif 48<= ord(a[n]) <=57 or 65<= ord(a[n]) <=90 or 97<= ord(a[n]) <=122: # 알파벳이나 숫자 만나면
        s=n
        while 48<= ord(a[n]) <=57 or 65<= ord(a[n]) <=90 or 97<= ord(a[n]) <=122:  # 알파벳이나 숫자가 아닐때까지 반복
            alpha.append(a[n])
            n+=1                # 뒤집기위해 따로 저장하고 인덱스+1
        alpha.reverse()
        for i in alpha:
            r[s]=i               # 뒤집은 단어 결과 리스트에 저장
            s+=1
    else:
        r[n]=a[n]
        n+=1                # r에 그대로 옮기고 인덱스+1
r=r[:-1]
r=''.join(r)
print(r)
