# https://www.codechef.com/problems/CCOOK

for T in range(int(input())):
    ans=["Beginner", "Junior Developer", "Middle Developer", "Senior Developer", "Hacker", "Jeff Dean"]
    print(ans[list(map(int,input().split())).count(1)])