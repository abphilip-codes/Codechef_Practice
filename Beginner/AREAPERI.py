# https://www.codechef.com/problems/AREAPERI

l,b=int(input()),int(input())
if(2*(l+b)>l*b): print("Peri\n{}".format(2*(l+b)))  
elif(2*(l+b)<l*b): print("Area\n{}".format(l*b))
else: print("Eq\n{}".format(l*b))