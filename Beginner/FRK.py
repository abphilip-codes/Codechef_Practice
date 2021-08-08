# https://www.codechef.com/problems/FRK

c,k=['ch','he','ef','che','hef','chef'],0
for T in range(int(input())):
    s=input()
    for i in c:
        if(i in s): 
            k+=1
            break
print(k)