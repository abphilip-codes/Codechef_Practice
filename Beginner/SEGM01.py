# https://www.codechef.com/problems/SEGM01

for T in range(int(input())): print("NO") if(len([s for s in input().split('0') if s])!=1) else print("YES")