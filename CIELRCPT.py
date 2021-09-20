# https://www.codechef.com/problems/CIELRCPT

for T in range(int(input())):
    s,n = 0,int(input())
    for z in range(11,-1,-1): s,n = s+(n//(2**z)),n%(2**z)
    print(s)