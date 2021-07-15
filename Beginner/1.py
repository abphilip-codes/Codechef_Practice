# https://www.codechef.com/problems/HS08TEST

x,y = map(float,input().split())
if(x%5==0 and (x+0.5)<=y): print("{:.2f}".format(y-x-0.5))
else: print("{:.2f}".format(y))