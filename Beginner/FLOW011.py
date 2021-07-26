# https://www.codechef.com/problems/FLOW011

for T in range(int(input())):
    n = int(input())
    print("{:.2f}".format(n*2)) if(n<1500) else print("{:.2f}".format(n*1.98+500))