# https://www.codechef.com/problems/CO92JUDG

for T in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    if((sum(A)-max(A))<(sum(B)-max(B))): print("Alice")
    elif((sum(A)-max(A))>(sum(B)-max(B))): print("Bob")
    else: print("Draw")