menu_items={"tea":80,"coffee":90,
            "pancake":100,"choco_cake":120,
            "ice_cream":70,"chicken":110
            }
#all keys
for k in menu_items.keys():
    print(k)

#all keys and values
for k,v in menu_items.items():
    print(k,v)

#all items below 100
for k,v in menu_items.items():
    if v<100:
        print(k)

#get price for ice_cream and chocolate
print(menu_items.get("ice_cream",0))
print(menu_items.get("chocolate",0))

#check if choco cake exist or not if yes then add 15 to its current price
if "choco_cake" in menu_items:
    menu_items["choco_cake"]+=15
print(menu_items)
