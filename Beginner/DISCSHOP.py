# https://www.codechef.com/problems/DISCSHOP

for _ in range(int(input())):
    n,m=input(),99999999999999
    for z in range(len(n)): m=min(m,int(n[:z]+n[z+1:]))
    print(m)