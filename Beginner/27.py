# https://www.codechef.com/problems/PRB01

for T in range(int(input())):
    n = int(input())
    if(n>1):
        for z in range(2,n):
            if(n%z==0): 
                print("no")
                break
        else: print("yes")
    else: print("no")