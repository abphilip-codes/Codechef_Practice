# https://www.codechef.com/problems/PERMUT2

while(int(input())):
    l = list(map(int,input().split()))
    for i in l:
        if(l[i-1]!=(l.index(i)+1)): 
            print("not ambiguous")
            break
    else: print("ambiguous")