# https://www.codechef.com/problems/T20MCH

r,o,c=map(int,input().split())
print("YES") if((r-c)/(20-o)<36) else print("NO")