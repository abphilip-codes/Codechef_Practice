# https://www.codechef.com/problems/RECIPE

def check(z,l=[]):
    for i in range(0,len(l)):
        if(l[i]%z!=0): return False
    return True
for T in range(int(input())):
    l = list(map(int,input().split()))[1:]
    for z in range(min(l),1,-1):
        if(check(z,l)==True): l[:] = [int(a/z) for a in l]
    print(*l)