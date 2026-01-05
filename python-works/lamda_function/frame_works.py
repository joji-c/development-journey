car_miles={
    "toyota":1000,
    "suzuki":1234,
    "bmw":2345,
    "benz":6253
}
"""#using key sort
srt=sorted(car_miles)
print(srt)

#using value sort
sorte=sorted(car_miles,key=car_miles.get)
print(sorte)
sorte=sorted(car_miles,key=car_miles.get,reverse=True)
print(sorte)"""

#using lambda and value sort
st=sorted(car_miles,key=lambda k:car_miles.get(k))
print(st)
st=sorted(car_miles,key=lambda k:car_miles.get(k),reverse=True)
print(st)