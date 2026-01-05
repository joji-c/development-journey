cibil_score = int(input("enter your cibil score: "))
if cibil_score>=300 and cibil_score<550:
    print("POOR")
elif cibil_score>=550 and cibil_score<650:
    print("AVERAGE")
elif cibil_score>=650 and cibil_score<700:
    print("GOOD")
elif cibil_score>=700 and cibil_score<=900:
    print("EXCELLENT")
else:
    print("Invalid input")
