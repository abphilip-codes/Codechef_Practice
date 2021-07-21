# https://www.codechef.com/problems/PERMUT2

def ans(l):
    z,c=[0]*len(l),1
    for i in l: z[i-1],c=c,c+1
    return z
while(int(input())>0):
    l = list(map(int,input().split()))
    print("ambiguous") if(l==ans(l)) else print("not ambiguous")