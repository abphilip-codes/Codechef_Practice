# https://www.codechef.com/problems/TWONMS

for T in range(int(input())):
    a,b,n=input().split()
    print(max(int(a)*2,int(b))//min(int(a)*2,int(b))) if(int(n[-1])%2!=0) else print(max(int(a),int(b))//min(int(a),int(b)))