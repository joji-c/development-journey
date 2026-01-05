height_in_cm = int(input("enter height in cm "))
weight_in_kg = int(input("enter weight in kg "))
height_in_m = height_in_cm/100
bmi = weight_in_kg/(height_in_m)**2
print(bmi)

#in this code we add int in front of input to change the type of input from string to integer
