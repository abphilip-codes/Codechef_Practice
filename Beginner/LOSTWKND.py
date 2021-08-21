# https://www.codechef.com/problems/LOSTWKND

for T in range(int(input())):
    l=list(map(int,input().split()))
    print("No") if(sum(l[:-1])*l[-1]<=120) else print("Yes")