a = int(input())
b = int(input())
c = int(input())
if (a>b) & (a>c):
    print(a)
elif (b>c) & (b>a):
    print(b)
else:
    print(c)