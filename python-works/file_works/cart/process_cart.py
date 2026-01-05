file_pth="python-works\\file_works\\cart\\cart_items_100.csv"
try:
    fr=open(file_pth,"r")
    import csv
    reader=csv.DictReader(fr)
    data=[row for row in reader]

    orders={}
    for d in data:
        title=d.get("title")
        qty=int(d.get("quantity"))
        if title in orders:
            orders[title]+=qty
        else:
            orders[title]=qty

    print(orders)

    max_order={k:v for k,v in orders.items() if v==max(orders.values())}
    print("max orders:",max_order)

    min_order={k:v for k,v in orders.items() if v==min(orders.values())}
    print("min orders:",min_order)

    users=[d.get("user") for d in data]
    user_c={u:users.count(u) for u in users}
    max_user={k:v for k,v in user_c.items() if v==max(user_c.values())}
    print("max purchased user:",max_user)

except Exception as e:
    print(e)

finally:
    fr.close()
