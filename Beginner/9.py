# https://www.codechef.com/problems/TSORT

n=[]
for T in range(int(input())):n.append(int(input()))
print(*sorted(n),sep="\n")