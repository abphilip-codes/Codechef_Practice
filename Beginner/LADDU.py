# https://www.codechef.com/problems/LADDU

for _ in range(int(input())):
    n,o=input().split()
    ans=0
    for z in range(int(n)):
        i = input().split()
        if(i[0]=='CONTEST_WON'): ans+=(300+max(0,20-int(i[1])))
        elif(i[0]=='TOP_CONTRIBUTOR'): ans+=300
        elif(i[0]=='BUG_FOUND'): ans+=int(i[1])
        elif(i[0]=='CONTEST_HOSTED'): ans+=50
    print(ans//(200 if(o=='INDIAN') else 400))