# https://www.codechef.com/problems/TTENIS

for T in range(int(input())):
    s=input()
    print("WIN") if(s.count('1')>s.count('0')) else print("LOSE")