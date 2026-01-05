import csv
class DogBreeds:
    data:list

    def __init__(self):
        file_path="python-works\\file_works\\dog\\dog_breeds.csv"
        fr=open(file_path,"r",encoding="utf-8")
        reader=csv.DictReader(fr)
        self.data=[r for r in reader]

    def dog_breeds(self):
        self.breed=[d.get("Breed") for d in self.data]
        self.breed_c={b:self.breed.count(b) for b in self.breed}
        print(self.breed_c)
        print("we have",len(self.breed_c.keys()),"different bread of dogs")

    def lab_orgin(self):
        self.lab_count=[d.get("Country of Origin") for d in self .data if d.get("Breed")=="Labrador Retriever"]
        print(self.lab_count)

    def england_breeds(self):
        self.eng_b=[d.get("Breed") for d in self .data if d.get("Country of Origin")=="England"]
        print("There are",len(self.eng_b),"in England")
        print("They are:",self.eng_b)

    def poodle_color(self):
        self.pood_col=[d.get("Fur Color") for d in self .data if "Poodle" in d.get("Breed")]
        self.col_c={p:self.pood_col.count(p) for p in self.pood_col}
        self.max_col=[k for k,v in self.col_c.items() if v== max(self.col_c.values())]
        print(self.max_col)

    def blue_eyes(self):
        self.blue_ey=[d.get("Breed") for d in self.data if "Blue" in d.get("Color of Eyes")]
        print(self.blue_ey)

    def german_height(self):
        self.ger_h=[d.get("Height (in)") for d in self .data if d.get("Breed")=="German Shepherd"]
        print(self.ger_h)

    def life_12_15(self):
        self.ls=[d.get("Breed") for d in self .data if d.get("Longevity (yrs)")=="12-15"]
        print(self.ls)
    
    def beagle_char(self):
        self.ls=[d.get("Character Traits") for d in self .data if d.get("Breed")=="Beagle"]
        print(self.ls)

    def common_disease(self):
        self.disease=[d.get("Common Health Problems") for d in self .data]
        self.disease_c={p:self.disease.count(p) for p in self.disease}
        self.common_dis=[k for k,v in self.disease_c.items() if v==max(self.disease_c.values())]
        print(self.common_dis)

    def lowest_lengevity(self):
        self.life=[d.get("Longevity (yrs)") for d in self.data]
        self.li=[]
        for l in self.life:
            l=l.split("-")
            self.li.append(int(l[0]))
            self.li.append(int(l[1]))
        self.min_n=str(min(self.li))+"-"
        self.min_breed={d.get("Breed"):d.get("Longevity (yrs)") for d in self.data if self.min_n in d.get("Longevity (yrs)")}
        print(self.min_breed)

dog_instance=DogBreeds()
#dog_instance.dog_breeds()
#dog_instance.lab_orgin()
#dog_instance.england_breeds()
#dog_instance.poodle_color()
#dog_instance.blue_eyes()
#dog_instance.german_height()
#dog_instance.life_12_15()
#dog_instance.beagle_char()
#dog_instance.common_disease()
#dog_instance.lowest_lengevity()
