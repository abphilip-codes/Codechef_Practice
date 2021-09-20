# https://www.codechef.com/problems/COLOR

for T in range(int(input())):
    n,l=int(input()),list(input())
    print(n-max(l.count('R'),l.count('G'),l.count('B')))