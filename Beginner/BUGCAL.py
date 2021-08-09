# https://www.codechef.com/problems/BUGCAL

for T in range(int(input())):
    l=input().split()
    z="0"*(len(max(l))-len(min(l)))
    print(z)