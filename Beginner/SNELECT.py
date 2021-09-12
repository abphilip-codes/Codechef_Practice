# https://www.codechef.com/problems/SNELECT

for _ in range(int(input())):
    st,a,z = "k"+input()+"k",[],1
    a = [f for f in st]
    while(a[z]!='k'): 
        if(a[z-1]=='s'): 
            a.pop(z-1)
            z-=1
        elif(a[z+1]=='s'): 
            a.pop(z+1)
        z+=1 
    print(a)