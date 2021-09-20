# https://www.codechef.com/problems/TRISQ

def add(n):
    s=0
    for z in range(n+1): s+=z
    return s
for T in range(int(input())):
    n = int(input())-3
    print(add((n+1)//2))