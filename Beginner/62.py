# https://www.codechef.com/problems/LONGSEQ

for T in range(int(input())):
    s=input()
    print("Yes") if(s.count('0')==1 or s.count('1')==1) else print("No")