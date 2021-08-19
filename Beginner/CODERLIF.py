# https://www.codechef.com/problems/CODERLIF

for T in range(int(input())):
    l,c=list(map(int,input().split())),0
    for i in range(30):
        if(l[i]==1): 
            c+=1 
            if(c>5): 
                print("#coderlifematters")
                break
        else: c=0 
    else: print("#allcodersarefun")