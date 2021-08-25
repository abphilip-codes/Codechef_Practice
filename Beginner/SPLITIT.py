# https://www.codechef.com/problems/SPLITIT

for T in range(int(input())):
    n,s=int(input()),input()
    for z in range(n//2,n):
        if(s[z:] in s[:z]): 
            print("YES")
            break
    else: print("NO")