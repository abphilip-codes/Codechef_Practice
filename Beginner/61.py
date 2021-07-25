# https://www.codechef.com/problems/LCH15JAB

for T in range(int(input())):
    a={}
    s=input()
    for i in s:
        if i in a: a[i]+=1 
        else: a[i]=1
    print("YES") if(s.count(max(a,key=a.get))==len(s)/2) else print("NO")