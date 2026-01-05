height_in_cm = int(input("enter height in cm "))
weight_in_kg = int(input("enter weight in kg "))
height_in_m = height_in_cm/100
bmi = weight_in_kg/(height_in_m)**2
bmi = round(bmi,0) #here we use round to remove decimal, and then specify how many decimal points are required if any
print("BMI score:",bmi)
if bmi in range(0,20):
    print("UNDER WEIGHT")
elif bmi in range(20,25):
    print("NORMAL")
elif bmi in range(25,30):
    print("OVER WEIGHT")
else:
    print("OBESE")

# here we us ethe range function
#it takes start and finishes with the n-1 number of what was given -> range(start,finish)

