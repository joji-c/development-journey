import csv
class IndianFood:
    def __init__(self):
        file_path="python-works\\file_works\\indian_food\\indian_food.csv"
        fr=open(file_path,"r",encoding="utf-8")
        self.read=csv.DictReader(fr)
        self.data=[r for r in self.read]

    def num_of_items(self):
        print("num of items:",len(self.data))

    def diet_type(self):
        self.diet={}
        for d in self.data:
            self.type=d.get("diet")
            if self.type in self.diet:
                self.diet[self.type]+=1
            else:
                self.diet[self.type]=1
        print(self.diet)

    def deserts(self):
       self.des=[d.get("name") for d in self.data if d.get("course")=="dessert"]
       print(self.des)
       print("number of deserts: ",len(self.des))

    def max_prep(self):
        self.mp=[d.get("name") for d in self.data if d.get("prep_time")==max(d.get("prep_time") for d in self.data)]
        print(self.mp)

    def min_prep(self):
        self.mp=[d.get("name") for d in self.data if d.get("prep_time")==min(d.get("prep_time") for d in self.data)]
        print(self.mp)

    def max_cook(self):
        self.mc=[d.get("name") for d in self.data if d.get("cook_time")==max(d.get("cook_time") for d in self.data)]
        print(self.mc)

    def min_cook(self):
        self.mc=[d.get("name") for d in self.data if d.get("cook_time")==min(d.get("cook_time") for d in self.data)]
        print(self.mc)

    def sweet_fl(self):
       self.sf=[d.get("name") for d in self.data if d.get("flavor_profile")=="sweet"]
       print(self.sf)
       print("number of sweet_fl: ",len(self.sf))

    def max_state(self):
        self.state={}
        for d in self.data:
            self.st=d.get("state")
            if self.st in self.state:
                self.state[self.st]+=1
            else:
                self.state[self.st]=1
        for k,v in self.state.items():
            if v==max(v for v in self.state.values()):
                print(k)

    def region_type(self):
        self.region={}
        for d in self.data:
            self.reg=d.get("region")
            if self.reg in self.region:
                self.region[self.reg]+=1
            else:
                self.region[self.reg]=1
        print(self.region)

    def w_bengal_dish(self):
        self.wb=[d.get("name") for d in self.data if d.get("state")=="West Bengal"]
        print(self.wb)
        print("number of west_bengal dish: ",len(self.wb))

    def avg_prep(self):
        self.sum=0
        for d in self.data:
            self.prep=int(d.get("prep_time"))
            self.sum+=self.prep
        print("average prep time: ",round(self.sum/len(self.data)))

    def avg_cook(self):
        self.sum=0
        for d in self.data:
            self.prep=int(d.get("cook_time"))
            self.sum+=self.prep
        print("average cook time: ",round(self.sum/len(self.data)))

    def ghee_used(self):
        self.gh=[d.get("name") for d in self.data if "ghee" in d.get('ingredients')]
        print(self.gh)
        print("num of ghee used food items:",len(self.gh))

    def course_type(self):
        self.course={}
        for d in self.data:
            self.co=d.get("course")
            if self.co in self.course:
                self.course[self.co]+=1
            else:
                self.course[self.co]=1
        print(self.course)

    def max_time(self):
        self.ht={}
        for d in self.data:
            self.prep=int(d.get("prep_time"))
            self.cook=int(d.get("cook_time"))
            self.name=d.get("name")
            self.sum=self.prep+self.cook
            if self.name in self.ht:
                self.ht[self.name]+=self.sum
            else:
                self.ht[self.name]=self.sum
        for k,v in self.ht.items():
            if v==max(v for v in self.ht.values()):
                print(k)

    def north_dish(self):
        self.nd=[d.get("name") for d in self.data if d.get("region")=="North"]
        print(self.nd)
        print("number of northern dish: ",len(self.nd))

    def spicy_fl(self):
       self.sf=[d.get("name") for d in self.data if d.get("flavor_profile")=="spicy"]
       print(self.sf)
       print("number of spicy_fl: ",len(self.sf))

    def common_ing(self):
        self.ing=[d.get("ingredients").split(',') for d in self.data]
        self.word=[]
        self.in_c={}
        for i in self.ing:
            for j in i:
                self.word.append(j)
        for w in self.word:
            if w in self.in_c:
                self.in_c[w]+=1
            else:
                self.in_c[w]=1
        for k,v in self.in_c.items():
            if v==max(v for v in self.in_c.values()):
                print("most commonly used ingredient:",k)

    def prep_ls_20(self):
        self.mp=[d.get("name") for d in self.data if int(d.get("prep_time"))<20]
        print(self.mp)
        print("num of dish with prep time less than 20:",len(self.mp))

    def veg_deserts(self):
       self.vdes=[d.get("name") for d in self.data if d.get("course")=="dessert" and d.get("diet")=="vegetarian"]
       print(self.vdes)
       print("number of vegetarian deserts: ",len(self.vdes))

food_instance=IndianFood()
#food_instance.num_of_items()
#food_instance.diet_type()
#food_instance.deserts()
#food_instance.max_prep()
#food_instance.min_prep()
#food_instance.max_cook()
#food_instance.min_cook()
#food_instance.sweet_fl()
#food_instance.max_state()
#food_instance.region_type()
#food_instance.w_bengal_dish()
#food_instance.avg_prep()
#food_instance.avg_cook()
#food_instance.ghee_used()
#food_instance.course_type()
#food_instance.max_time()
#food_instance.north_dish()
#food_instance.spicy_fl()
#food_instance.common_ing()
#food_instance.prep_ls_20()
#food_instance.veg_deserts()
