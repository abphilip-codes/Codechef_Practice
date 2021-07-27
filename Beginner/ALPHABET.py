# https://www.codechef.com/problems/ALPHABET

s=input()
for T in range(int(input())): print("Yes") if(set(s)==set(input())) else print("No")