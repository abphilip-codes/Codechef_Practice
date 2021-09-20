# https://www.codechef.com/problems/ATTENDU

for _ in range(int(input())):
    n,l,count=int(input()),input(),0
    for z in range(n):
        if(l[z]=='1'): count+=1
    print('YES') if(count+(120-n)>=90) else print('NO')