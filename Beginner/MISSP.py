# https://www.codechef.com/problems/MISSP

for T in range(int(input())):
    a=[]
    for n in range(int(input())):
        k=int(input())
        if(k not in a): a.append(k)
        else: a.remove(k)
    print(a[0])