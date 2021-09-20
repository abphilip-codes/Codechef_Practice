# https://www.codechef.com/problems/PLAYSTR

for T in range(int(input())):
    n,s,r=int(input()),input(),input()
    print("YES") if(s.count('1')==r.count('1')) else print("NO")