import csv
class Ai_Impact:
    data:list

    def __init__(self):
        file_path="python-works\\object-oriented-programming\\inheritance\\ai-impact\\AI_Impact_on_Jobs_2030.csv"
        fr=open(file_path,"r",encoding="utf-8")
        reader=csv.DictReader(fr)
        self.data=[r for r in reader]
    
    def total_count(self):
        print(f"Total entry count:{len(self.data)}")

    def first_entry(self):
        print(self.data[0])

ai_instance1=Ai_Impact()
ai_instance1.total_count()
ai_instance1.first_entry()
