# https://www.codechef.com/problems/ANKTRAIN

for T in range(int(input())):
    n=int(input())
    d,r=n//8,n%8
    if(r in [1,4]): 
        if(r>3): r-=3
        else: r+=3
        print("{}LB".format(8*d+r))
    elif(r in [2,5]): 
        if(r>3): r-=3
        else: r+=3
        print("{}MB".format(8*d+r))
    elif(r in [3,6]):
        if(r>3): r-=3
        else: r+=3
        print("{}UB".format(8*d+r))
    else: 
        if(r==0): print("{}SL".format(8*(d-1)+7))
        elif(r==7): print("{}SU".format(8*(d+1)))