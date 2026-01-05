#daily_calory_consumption(height,weight,age,gender,activity=1.2,goal,target,duration)
#1kg = 7700cal

def daily_calory_consumption(gender,weight,height,age,target,duration,goal="loss",activity=1.2):
    if gender == "male":
        bmr=10*weight+6.25*height-5*age+5
    else:
        bmr=10*weight+6.25*height-5*age-161
    calory = bmr*activity
    consumption = (target*7700)//(duration*30)
    daily = calory- consumption
    return daily

print(daily_calory_consumption("male",64,160,22,4,2))
    