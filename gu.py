S1=int(input())
a1=list(map(int,input().split()))[:S1]
av=int(n/2)
L=a1[:av]
M=a1[av::]
if sum(L)//len(L)==sum(M)//len(M):
    print("yes")
else:
    print("no")
