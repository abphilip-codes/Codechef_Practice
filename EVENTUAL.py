# https://www.codechef.com/problems/EVENTUAL

for T in range(int(input())):
    n,s=int(input()),input()
    for z in range(97,123):
        if(s.count(chr(z))%2!=0): 
            print("NO")
            break
    else: print("YES")