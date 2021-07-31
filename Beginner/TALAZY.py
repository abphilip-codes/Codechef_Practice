# https://www.codechef.com/problems/TALAZY

for T in range(int(input())):
    N,B,M=map(int,input().split())
    ans,N=((N+1)//2)*M,N-((N+1)//2)
    while(N):
        ans,M=ans+B,M*2
        ans,N=ans+((N+1)//2)*M,N-((N+1)//2)
    print(ans)