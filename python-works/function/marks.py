def grade(marks):
    if marks>=90 and marks<=100:
        return "A grade"
    elif marks>=75 and marks<90:
        return "B grade"
    elif marks>=50 and marks<75:
        return "C grade"
    elif marks>=0 and marks<50:
        return "F grade"
    else:
        return "Invalid input"
    

print(grade(92))
print(grade(67))
