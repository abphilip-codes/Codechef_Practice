# https://www.codechef.com/problems/C00K0FF

for T in range(int(input())):
    l,ans=[],0
    for z in range(int(input())):
        l.append(input())
    if(l.count('cakewalk')>=1 and l.count('simple')>=1 and l.count('easy')>=1):
        if((l.count('easy-medium')>=1 or l.count('medium')>=1) and (l.count('medium-hard')>=1 or l.count('hard')>=1)): ans=1
    print("Yes") if(ans==1) else print("No")