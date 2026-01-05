#check bmi
def bmi(height,weight):
    hm=height/100
    result=weight/(hm**2)
    return round(result)

print(bmi(160,64))
