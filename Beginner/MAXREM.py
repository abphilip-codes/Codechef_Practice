# https://www.codechef.com/problems/MAXREM

n,l=int(input()),sorted(set(list(map(int, input().split()))))
print(l[-2]%l[-1]) if(len(l)>1) else print(0)