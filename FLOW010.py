# https://www.codechef.com/problems/FLOW010

l = ['BattleShip','Cruiser','Destroyer','Frigate']
for T in range(int(input())):
    n = input().upper()
    for i in l:
        if(n==i[0]): print(i)