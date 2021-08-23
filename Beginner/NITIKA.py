# https://www.codechef.com/problems/NITIKA

for T in range(int(input())):
    l,ans=list(map(str,input().split(" "))),[]
    for z in range(len(l)-1): ans.append(str(l[z][0]).upper()+".")
    ans.append(l[-1][0].upper()+l[-1][1:].lower())
    print(*ans)