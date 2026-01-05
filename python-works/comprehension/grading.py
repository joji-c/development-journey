#grading marks
dic1={"aju":92,"binu":76,"chandru":64}
grade={k:("A" if v>=90 else
          "B" if v>=70 else "C") for k,v in dic1.items()}
print(grade)


#ping pong
lis1=[4,6,3,7,5,9]
dic2={l:"ping" if l<5 else
        "pong" if l>5 else
        "pingpong" for l in lis1}
print(dic2)
