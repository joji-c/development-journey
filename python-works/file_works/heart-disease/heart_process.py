import csv
class HeartDisease:

    def __init__(self):
        file_path="python-works\\file_works\\heart-disease\\Heart_Disease_Prediction.csv"
        fr=open(file_path,"r",encoding="utf-8")
        reader=csv.DictReader(fr)
        self.data=[r for r in reader]

    def total_num_of_patients(self):
        print("Total patient number:",len(self.data))
    
    def heart_issue_have(self):
        self.hc={}
        for d in self.data:
            self.heart=d.get("Heart Disease")
            if self.heart in self.hc:
                self.hc[self.heart]+=1
            else:
                self.hc[self.heart]=1
        print(self.hc)

    def average_age(self):
        self.age=[int(d.get("Age")) for d in self.data]
        self.sum=0
        for a in self.age:
            self.sum+=a
        print("Average age:",round(self.sum/len(self.age)))


    def max_cholestrol_level(self):
        self.chol=[int(d.get("Cholesterol")) for d in self.data]
        print("Max cholestrol level:",max(self.chol))

    def gender_count(self):
        self.gen={}
        for d in self.data:
            self.gender=d.get("Sex")
            if self.gender in self.gen:
                self.gen[self.gender]+=1
            else:
                self.gen[self.gender]=1
        print(self.gen)

    def common_chest_pain(self):
        self.chest=[int(d.get("Chest pain type")) for d in self.data]
        self.chest_c={c:self.chest.count(c) for c in self.chest}
        self.max_chest_c=[k for k,v in self.chest_c.items() if v==max(self.chest_c.values())]
        print(self.max_chest_c)

    def avg_bp(self):
        self.bp=[int(d.get("BP")) for d in self.data]
        self.sum_bp=0
        for b in self.bp:
            self.sum_bp+=b
        print("Average bp:",round(self.sum_bp/len(self.bp)))

    def blood_sugar_over_120(self):
        self.count=0
        for d in self.data:
            self.bs=d.get("FBS over 120")
            if self.bs=="1":
                self.count+=1
        print(self.count)

    def avg_max_hr(self):
        self.hr=[int(d.get("Max HR")) for d in self.data]
        self.sum_hr=0
        for h in self.hr:
            self.sum_hr+=h
        print("Average hr:",round(self.sum_hr/len(self.hr)))

    def common_thalium_test_result(self):
        self.tal_test=[int(d.get("Thallium")) for d in self.data]
        self.tal_c={c:self.tal_test.count(c) for c in self.tal_test}
        self.max_tal_c=[k for k,v in self.tal_c.items() if v==max(self.tal_c.values())]
        print(self.max_tal_c)


heart_instance=HeartDisease()
#heart_instance.total_num_of_patients()
#heart_instance.heart_issue_have()
#heart_instance.average_age()
#heart_instance.max_cholestrol_level()
#heart_instance.gender_count()
#heart_instance.common_chest_pain()
#heart_instance.avg_bp()
#heart_instance.blood_sugar_over_120()
#heart_instance.avg_max_hr()
#heart_instance.common_thalium_test_result()
