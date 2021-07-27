# https://www.codechef.com/problems/CANDY123

for T in range(int(input())):
    l,n=list(map(int,input().split())),1
    while((n**2)<=l[0] and (n*(n+1))<=l[1]): n+=1 
    print("Bob") if((n*n)>l[0]) else print("Limak")