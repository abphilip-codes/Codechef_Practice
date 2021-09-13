# https://www.codechef.com/problems/SNELECT

for _ in range(int(input())):
    st,a = "k"+input()+"k",[]
    a = [f for f in st]
    for z in range(1,len(a)-1):
        if(a[z]=='m' and a[z-1]=='s'): a[z-1]="*"
        elif(a[z]=='m' and a[z+1]=='s'): a[z+1]="*"
    if(a.count('m')>a.count('s')): print("mongooses")
    elif(a.count('m')<a.count('s')): print("snakes")
    else: print("tie")