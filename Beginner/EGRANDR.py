# https://www.codechef.com/problems/EGRANDR

for T in range(int(input())):
    n,l=int(input()),list(map(int,input().split()))
    print("Yes") if(sum(l)/n>=4 and all(z>2 for z in l)) else print("No")