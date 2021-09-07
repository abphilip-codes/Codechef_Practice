# https://www.codechef.com/problems/ACBALL

for _ in range(int(input())):
    a,b,k=input(),input(),""
    for z in range(len(a)):
        if(a[z]==b[z]):
            if(a[z]=='W'): k+='B'
            else: k+='W'
        else: k+='B'
    print(k)