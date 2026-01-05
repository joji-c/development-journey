#break stops the iterations and gets out of the loop
for i in range(1,51):
    if i==25:
        break
    print(i)
print("last line")#here it will print till 24 then exit the loop and print last line

#continue skips a single iteration and continues the loop
for i in range(1,51):
    if i==25:
        continue
    print(i)#here the number 25 will be skipped every other number will be displayed
    