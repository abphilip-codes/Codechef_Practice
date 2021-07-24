# https://www.codechef.com/problems/MNMX

for T in range(int(input())):
    n,a=int(input()),list(map(int,input().split()))
    print((n-1)*min(a))
    # If order matters 
    # s=0 
    # for z in range(n-1): 
    #     if(a[0]>=a[1]):
    #         s+=a[1]
    #         a.pop(0) 
    #     else:
    #         s+=a[0]
    #         a.pop(1)
    # print(s)