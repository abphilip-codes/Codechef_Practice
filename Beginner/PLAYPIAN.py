# https://www.codechef.com/problems/PLAYPIAN

for T in range(int(input())):
    s=input()
    for i in range(0,len(s),2):
        if(s[i]==s[i+1]):
            print("no")
            break
    else: print("yes")