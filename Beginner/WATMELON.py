# https://www.codechef.com/problems/WATMELON

for T in range(int(input())):
    n,l=int(input()),list(map(int,input().split()))
    for z in range(n):
        if(l[z]%z!=0):
            print("NO")
            break
    else: print("YES")