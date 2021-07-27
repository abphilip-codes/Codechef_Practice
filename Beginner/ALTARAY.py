# https://www.codechef.com/problems/ALTARAY

s=input()
for T in range(int(input())): print("Yes") if(set(input()).issubset(set(s))) else print("No")