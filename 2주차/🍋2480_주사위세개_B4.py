a, b, c=map(int, input().split())
if a==b:
    if b==c:
        print(str(10000+a*1000))
    elif b!=c:
        print(str(1000+a*100))
elif b==c:
    if a==b:
        print(str(10000+a*1000))
    elif a!=b:
        print(str(1000+b*100))
elif a==c:
    if a==b:
        print(str(10000+a*1000))
    elif a!=b:
        print(str(1000+a*100))
else:
    if a>b and a>c:
        print(str(a*100))
    elif b>a and b>c:
        print(str(b*100))
    elif c>b and c>a:
        print(str(c*100))
        
