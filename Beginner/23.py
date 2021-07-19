# https://www.codechef.com/problems/AMR15A

N = int(input())
l = list(map(int,input().split()))
print("READY FOR BATTLE") if len(list(filter(lambda x:x%2==0,l)))>len(list(filter(lambda x:x%2!=0,l))) else print("NOT READY")