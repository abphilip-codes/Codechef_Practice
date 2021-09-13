# https://www.codechef.com/problems/CFMM

for _ in range(int(input())): 
    s=""
    for n in range(int(input())): s+=input()
    print(min(s.count('c')//2,s.count('e')//2,s.count('o'),s.count('d'),s.count('h'),s.count('f')))