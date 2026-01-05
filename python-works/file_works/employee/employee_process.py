import csv
class Employee:
    def __init__(self):
        file_path="python-works\\object-oriented-programming\\inheritance\\employee\\employee_salary_dataset.csv"
        fr=open(file_path,"r",encoding="utf-8")
        self.read=csv.DictReader(fr)
        self.data=[r for r in self.read]

    def highest_salary(self):
        self.id_sal={d.get("Name"):int(d.get("Monthly_Salary")) for d in self.data}
        self.max_sal=[k for k,v in self.id_sal.items() if v==max(self.id_sal.values())]
        print(self.max_sal)

    def avg_salary(self):
        self.sal=[int(d.get("Monthly_Salary")) for d in self.data]
        print("Average salary:",round(sum(self.sal)/len(self.sal)))

    def dep_emp_num(self):
        self.dep=[d.get("Department") for d in self.data]
        self.dep_c={}
        for d in self.dep:
            if d in self.dep_c:
                self.dep_c[d]+=1
            else:
                self.dep_c[d]=1
        print(self.dep_c)

    def avg_exp_dep(self):
        self.avg_exp={}
        for d in self.data:
            self.dep=d.get("Department")
            self.exp=int(d.get("Experience_Years"))
            if self.dep in self.avg_exp:
                self.avg_exp[self.dep]+=self.exp
            else:
                self.avg_exp[self.dep]=self.exp
        
        for k,v in self.avg_exp.items():
            v=v/len(self.data)
            print(k,v)

    def high_emp_city(self):
        self.city=[d.get("City") for d in self.data]
        self.city_c={c:self.city.count(c) for c in self.city}
        self.max_city={k:v for k,v in self.city_c.items() if v==max(self.city_c.values())}
        print(self.max_city)

    def edu_sal(self):
        self.mean_edu_sal={}
        for d in self.data:
            self.edu=d.get("Education_Level")
            self.sal=int(d.get("Monthly_Salary"))
            if self.edu in self.mean_edu_sal:
                self.mean_edu_sal[self.edu]+=self.sal
            else:
                self.mean_edu_sal[self.edu]=self.sal

        for k,v in self.mean_edu_sal.items():
            v=round(v/len(self.data))
            print(k,v)

    def max_avg_sal_dep(self):
        self.avg_sal={}
        for d in self.data:
            self.dep=d.get("Department")
            self.sal=int(d.get("Monthly_Salary"))
            if self.dep in self.avg_sal:
                self.avg_sal[self.dep]+=self.sal
            else:
                self.avg_sal[self.dep]=self.sal
        
        for k,v in self.avg_sal.items():
            v=round(v/len(self.data))
            self.avg_sal[k]=v
        
        self.max_sal_dep={k:v for k,v in self.avg_sal.items() if v==max(self.avg_sal.values())}
        print(self.max_sal_dep)

    def gender_count(self):
        self.gen=[d.get("Gender") for d in self.data]
        self.gen_c={g:self.gen.count(g) for g in self.gen}
        print(self.gen_c)

    def min_max_avg_age(self):
        self.age=[int(d.get("Age")) for d in self.data]
        print("Max age:",max(self.age))
        print("Min age:",min(self.age))
        print("Avg age:",round(sum(self.age)/len(self.age)))

    def common_edu_level(self):
        self.edu=[d.get("Education_Level") for d in self.data]
        self.edu_c={c:self.edu.count(c) for c in self.edu}
        self.common_edu={k:v for k,v in self.edu_c.items() if v==max(self.edu_c.values())}
        print(self.common_edu)



emp_instance=Employee()
#emp_instance.highest_salary()
#emp_instance.avg_salary()
#emp_instance.dep_emp_num()
#emp_instance.avg_exp_dep()
#emp_instance.high_emp_city()
#emp_instance.edu_sal()
#emp_instance.max_avg_sal_dep()
#emp_instance.gender_count()
#emp_instance.min_max_avg_age()
#emp_instance.common_edu_level()
