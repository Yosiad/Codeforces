n,m,a = list(map(int, input().split()))
sid1,sid2=0,0
if n%a==0: sid1=n//a
else: sid1=n//a+1
if m%a==0: sid2=m//a
else: sid2=m//a+1

print(sid2*sid1)
