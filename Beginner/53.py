# https://www.codechef.com/problems/CHN09

for T in range(int(input())):
    n=list(input())
    print(n.count('b')) if(n.count('b')<n.count('a')) else print(n.count('a'))