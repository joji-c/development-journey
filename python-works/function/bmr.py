
def daily_calory(gender,weight,height,age,activity=1.2):
    if gender == "male":
        bmr=10*weight+6.25*height-5*age+5
    else:
        bmr=10*weight+6.25*height-5*age-161
    return bmr*activity

print(daily_calory("male",64,160,22))
print(daily_calory("female",64,160,22))
