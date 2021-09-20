# https://www.codechef.com/problems/PALL01

for T in range(int(input())):
    n = input() 
    print("wins") if n==n[::-1] else print("loses")