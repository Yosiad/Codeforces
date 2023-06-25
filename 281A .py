n=input()
if ord(n[0])>96:
    print(chr(ord(n[0])-32)+n[1:])
else: print(n)
