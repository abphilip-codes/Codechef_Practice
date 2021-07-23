# https://www.codechef.com/problems/AREAPERI

l,b=int(input()),int(input())
print("Peri\n{}".format(2*(l+b))) if(2*(l+b)>l*b) else print("Area\n{}".format(l*b))