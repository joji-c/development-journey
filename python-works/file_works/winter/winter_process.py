import csv
class WinterFashion:
    def __init__(self):
        file_path="python-works\\object-oriented-programming\\inheritance\\winter\\Winter_Fashion_Trends_Dataset.csv"
        fr=open(file_path,"r",encoding="utf-8")
        reader=csv.DictReader(fr)
        self.data=[r for r in reader]
    
    def popular_cato(self):
        self.pop_cato={d.get("Category"):float(d.get("Popularity_Score")) for d in self.data}
        self.max_cato={k:v for k,v in self.pop_cato.items() if v==max(self.pop_cato.values())}
        print(self.max_cato)

    def brand_items(self):
        self.br_count={}
        for d in self.data:
            self.brand=d.get("Brand")
            if self.brand in self.br_count:
                self.br_count[self.brand]+=1
            else:
                self.br_count[self.brand]=1
        self.max_item={k:v for k,v in self.br_count.items() if v==max(self.br_count.values())}
        print(self.max_item)
    
    def avg_price(self):
        self.pr_sum=0
        for d in self.data:
            self.pri=float(d.get("Price(USD)"))
            self.pr_sum+=self.pri
        print("Average price:",round(self.pr_sum/len(self.data)))

    def exp_cato(self):
        self.cat_pri={}
        self.cato={}
        for d in self.data:
            self.cat=d.get("Category")
            self.pri=float(d.get("Price(USD)"))
            if self.cat in self.cat_pri:
                self.cat_pri[self.cat]+=self.pri
                self.cato[self.cat]+=1
            else:
                self.cat_pri[self.cat]=self.pri
                self.cato[self.cat]=1
            self.avg_pri={}
            for k,v in self.cat_pri.items():
                self.avg=round(self.cat_pri.get(k)/self.cato.get(k))
                self.avg_pri[k]=self.avg
        self.min_cato_avg={k:v for k,v in self.avg_pri.items() if v==min(self.avg_pri.values())}
        print(self.min_cato_avg)
  
    def high_cust_rating(self):
        self.cat_rat={}
        for d in self.data:
            self.cat=d.get("Category")
            self.cust=float(d.get("Customer_Rating"))
            if self.cat in self.cat_rat:
                self.cat_rat[self.cat]+=self.cust
            else:
                self.cat_rat[self.cat]=self.cust
        self.max_rat={k:v for k,v in self.cat_rat.items() if v==max(self.cat_rat.values())}
        print(self.max_rat)

    def avg_gen(self):
        self.gen_pri={}
        self.gen={}
        for d in self.data:
            self.gend=d.get("Gender")
            self.pri=float(d.get("Price(USD)"))
            if self.gend in self.gen_pri:
                self.gen_pri[self.gend]+=self.pri
                self.gen[self.gend]+=1
            else:
                self.gen_pri[self.gend]=self.pri
                self.gen[self.gend]=1
            self.avg_gen_pri={}
            for k,v in self.gen_pri.items():
                self.avg=round(self.gen_pri.get(k)/self.gen.get(k))
                self.avg_gen_pri[k]=self.avg
        print(self.avg_gen_pri)

    def common_mat(self):
        self.mat_count={}
        for d in self.data:
            self.mat=d.get("Material")
            if self.mat in self.mat_count:
                self.mat_count[self.mat]+=1
            else:
                self.mat_count[self.mat]=1
        self.max_mat={k:v for k,v in self.mat_count.items() if v==max(self.mat_count.values())}
        print(self.max_mat)

    def pri_rat(self):
        self.max_rat={d.get("Price(USD)"):float(d.get("Customer_Rating")) for d in self.data if float(d.get("Customer_Rating"))==max(float(d.get("Customer_Rating")) for d in self.data)}
        self.min_rat={d.get("Price(USD)"):float(d.get("Customer_Rating")) for d in self.data if float(d.get("Customer_Rating"))==min(float(d.get("Customer_Rating")) for d in self.data)}
        print(f"high rating:{list(self.max_rat.values())} price:{list(self.max_rat.keys())}")
        print(f"low rating:{list(self.min_rat.values())} price:{list(self.min_rat.keys())}")

    def trending_style(self):
        self.style_c={}
        for d in self.data:
            self.sty=d.get("Style")
            self.tren=d.get("Trend_Status")
            if self.tren=="Trending":
                if self.sty in self.style_c:
                    self.style_c[self.sty]+=1
                else:
                    self.style_c[self.sty]=1
        print(self.style_c)

    def exp_product(self):
        self.exp_pro=[d for d in self.data if float(d.get("Price(USD)"))==max(float(d.get("Price(USD)")) for d in self.data)]
        for e in self.exp_pro:
            print("brand:",e.get("Brand"))
            print("season:",e.get("Season"))
            print("price:",e.get("Price(USD)"))
        

fashion_instance=WinterFashion()
#fashion_instance.popular_cato()
#fashion_instance.brand_items()
#fashion_instance.avg_price()
#fashion_instance.exp_cato()
#fashion_instance.high_cust_rating()
#fashion_instance.avg_gen()
#fashion_instance.common_mat()
#fashion_instance.pri_rat()
#fashion_instance.trending_style()
#fashion_instance.exp_product()
