num=int(input())
if (num%2==0 and num%5==0) or (num%2!=0 and num%5==0):
    print("not weird")
elif(num%6==0 and num%20==0):
    print("weird")
elif(num%2==0 and num>=20):
    print("not weird")
else:
    print("weird")