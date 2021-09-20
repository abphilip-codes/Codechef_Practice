# https://www.codechef.com/problems/ENCMSG

for T in range(int(input())):
    n,s,st=int(input()),input(),""
    for i in range(0,n-1,2):
        print(chr(219-ord(s[i+1])),end="")
        print(chr(219-ord(s[i])),end="")
    print(chr(219-ord(s[n-1])),end="") if(n%2!=0) else print("",end="")
    print()