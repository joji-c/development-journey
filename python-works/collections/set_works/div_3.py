python_students={"alice","bob","charlie"}
ml_students={"bob","david","eve"}
print("student in both courses:",python_students.union(ml_students))
print("students in only python:",python_students.difference(ml_students))
print("students in only ml:",ml_students.difference(python_students))