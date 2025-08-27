num=[1,2,3,4,5,6,7]
def findminandmax(numbers):
    if not numbers:
        return None
    minvalue=maxvalue=numbers[0]
    for num in numbers[1:]:
        if num<minvalue:
            minvalue=num
        elif num>maxvalue:
            maxvalue=num
    return minvalue,maxvalue
minimum,maximum=findminandmax(num)
print("minimum:",minimum)
print("maximum:",maximum)