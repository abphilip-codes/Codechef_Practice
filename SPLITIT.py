# https://www.codechef.com/problems/SPLITIT

for T in range(int(input())):
    n,s=int(input()),input()
    if(s[n-1] in s[:n-1]): print("YES")
    else: print("NO")