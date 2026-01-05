def emi(prin,int_rate,loan_tenure):
    result = (prin*int_rate*(1+int_rate)**loan_tenure) / ((1+int_rate)**loan_tenure-1)
    return round(result)

print(emi(10000,10,2))