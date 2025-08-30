from functools import reduce
num=[25,15,5,77,123,9]
result=reduce(lambda a,b:a+b,num)
result1=reduce(lambda a,b:a if a>b else b,num)
result2=reduce(lambda a,b:a if a<b else b,num)
print(result)
print(result1)
print(result2)
