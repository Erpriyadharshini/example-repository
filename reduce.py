from functools import reduce
num=[25,15,5,77,123,9]
min=reduce(lambda a,b:a if a<b else b,num)
max=reduce(lambda a,b:a if a>b else b,num)
print(min)
print(max)
