# https://www.codechef.com/problems/TWTCLOSE

n,t = map(int,input().split())
l = [0]*n
for T in range(t):
    s = input().split()
    if(s[0]=='CLOSEALL'): l = [0]*n
    else: l[int(s[1])-1]=(l[int(s[1])-1]+1)%2
    print(l.count(1))