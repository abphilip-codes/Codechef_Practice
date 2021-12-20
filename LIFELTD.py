# https://www.codechef.com/problems/LIFELTD

for T in range(int(input())):
    a,c = [input() for _ in range(3)],0
    for z in range(1,3):
        for y in range(0,2):
            if(a[z][y]=='l'):
                if(a[z-1][y]=='l' and a[z][y+1]=='l'): c=1
    print('yes') if(c) else print('no')