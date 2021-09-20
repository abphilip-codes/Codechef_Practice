# https://www.codechef.com/problems/NW1

for T in range(int(input())):
    w,s=map(str,input().split())
    days,ans=["mon", "tues", "wed", "thurs", "fri", "sat", "sun"],[4]*7
    for z in range(0,int(w)-28): ans[(z+days.index(s))%7]+=1
    print(*ans)