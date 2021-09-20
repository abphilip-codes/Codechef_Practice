# https://www.codechef.com/problems/QUADROOT

a,b,c=int(input()),int(input()),int(input())
if(b*b-4*a*c>=0):
    print(int((-b+(b*b-4*a*c)**(1/2))/2*a))
    print(int((-b-(b*b-4*a*c)**(1/2))/2*a))