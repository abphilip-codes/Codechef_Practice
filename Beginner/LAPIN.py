# https://www.codechef.com/problems/LAPIN

for T in range(int(input())):
    l = list(input())
    print("YES") if(sorted(l[0:len(l)//2])==sorted(l[(len(l)+1)//2:len(l)])) else print("NO")