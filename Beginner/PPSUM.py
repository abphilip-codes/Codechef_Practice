# https://www.codechef.com/problems/PPSUM

def allen(d,n):
    if(d==0): return n
    else: return allen(d-1,sum(range(1,n+1)))
for T in range(int(input())):
    d,n = map(int,input().split())
    print(allen(d,n))