# https://www.codechef.com/problems/FLOW015

for T in range(int(input())):
    n,days,c=int(input()),['sunday','monday','tuesday','wednesday','thursday','friday','saturday'],1
    if(n>2001):
        for z in range(2002,n+1):
            if((z-1)%4==0 and ((z-1)%400==0 or (z-1)%100!=0)): c+=2 
            else: c+=1
    else:
        for z in range(2000,n-1,-1):
            if(z%4==0 and (z%400==0 or z%100!=0)): c-=2 
            else: c-=1
    print(days[c%7])