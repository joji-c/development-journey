def disp_num(limit):
    if limit==0:
        return 
    print (limit)
    return disp_num(limit-1)

disp_num(15)
