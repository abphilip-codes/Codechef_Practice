# https://www.codechef.com/problems/RAINBOWA

for T in range(int(input())):
    n,l=int(input()),list(map(int,input().split()))
    print("no") if(set(l)!=set(list(range(1,8))) or l[0]!=1 or l[-1]!=1 or l!=l[::-1]) else print("yes")