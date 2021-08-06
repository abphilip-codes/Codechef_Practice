# https://www.codechef.com/problems/LOSTMAX

for T in range(int(input())):
    l=list(map(int,input().split()))
    l.remove(len(l)-1)
    print(max(l))