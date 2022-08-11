inp = int(input())
a = [1]*inp

for i in range(1,inp):
    a[i] = a[i-1]+2

for num in a:
    b= '#'*num
    print(b.center(a[-1]))