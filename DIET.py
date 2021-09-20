# https://www.codechef.com/problems/DIET

for T in range(int(input())):
    n,k=map(int,input().split())
    a,p=list(map(int,input().split())),0
    for z in range(len(a)):
        if(p+a[z]<k): 
            print("NO {}".format(z+1))
            break
        else: p=p+a[z]-k
    else: print("YES")