# https://www.codechef.com/problems/BRKBKS

def allen(s,a):
    if (len(a)==0): return 0
    elif (sum(a)<=s): return 1
    return 1+min(allen(s,a[1:]),allen(s,a[-2::-1]))
for _ in range(int(input())):
	l = list(map(int,input().split()))
	print(min(allen(l[0],l[1:]),allen(l[0],l[1:][::-1])))