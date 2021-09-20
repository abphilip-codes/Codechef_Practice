# https://www.codechef.com/problems/SNAKPROC

for T in range(int(input())):
    n,s,check=int(input()),input(),0
    for i in s:
        if(i=="H"): check+=1 
        elif(i=="T"): check-=1 
        if(check<0 or check>1): 
            print("Invalid")
            break
    else:
        print("Valid") if(check==0) else print("Invalid")