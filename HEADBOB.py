# https://www.codechef.com/problems/HEADBOB

for T in range(int(input())):
    n,s = int(input()),input()
    if("I" in s): print("INDIAN")
    elif(s.count("N")==len(s)): print("NOT SURE")
    else: print("NOT INDIAN")