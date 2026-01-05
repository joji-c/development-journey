import csv
class Covid:
    def __init__(self):
        file_path="python-works\\file_works\\covid\\country_wise_latest_covid.csv"
        fr=open(file_path,"r",encoding="utf-8")
        reader=csv.DictReader(fr)
        self.data=[r for r in reader]
    
    def most_affected(self):
        self.most_c=[d.get("Country/Region") for d in self.data if int(d.get("Confirmed"))==max(int(d.get("Confirmed")) for d in self.data)]
        print(self.most_c)

    def most_deaths(self):
        self.most_d=[d.get("Country/Region") for d in self.data if int(d.get("Deaths"))==max(int(d.get("Deaths")) for d in self.data)]
        print(self.most_d)

    def total_deaths(self):
        self.sum=0
        for d in self.data:
            self.de=int(d.get("Deaths"))
            self.sum+=self.de
        print(self.sum)

    def max_death_by_100(self):
        self.most_dea={d.get("Country/Region"):d.get("Deaths / 100 Cases") for d in self.data if float(d.get("Deaths / 100 Cases"))==max(float(d.get("Deaths / 100 Cases")) for d in self.data)}
        print(self.most_dea) 

    def most_active(self):
        self.most_a=[d.get("Country/Region") for d in self.data if float(d.get("Active"))==max(float(d.get("Active")) for d in self.data)]
        print(self.most_a) 

    def most_recovered(self):
        self.most_r=[d.get("Country/Region") for d in self.data if float(d.get("Recovered"))==max(float(d.get("Recovered")) for d in self.data)]
        print(self.most_r)

    def lowest_recovery_rate(self):
        self.most_r={d.get("Country/Region"):float(d.get("Recovered")) for d in self.data if float(d.get("Recovered"))==max(float(d.get("Recovered")) for d in self.data)}
        print(self.most_r)

    def max_recovered_by_100(self):
        self.most_re={d.get("Country/Region"):float(d.get("Recovered / 100 Cases")) for d in self.data if float(d.get("Recovered / 100 Cases"))==max(float(d.get("Recovered / 100 Cases")) for d in self.data)}
        print(self.most_re)  

    def max_death_by_recovered(self):
        self.most_rec={d.get("Country/Region"):d.get("Deaths / 100 Recovered") for d in self.data if float(d.get("Deaths / 100 Recovered").replace('inf','0'))==max(float(d.get("Deaths / 100 Recovered").replace('inf','0')) for d in self.data)}
        print(self.most_rec)

    def most_affected_who(self):
        self.most_c=[d.get("WHO Region") for d in self.data if d.get("Confirmed")==max(d.get("Confirmed") for d in self.data)]
        print(self.most_c)

    def most_deaths_who(self):
        self.most_d=[d.get("WHO Region") for d in self.data if float(d.get("Deaths"))==max(float(d.get("Deaths")) for d in self.data)]
        print(self.most_d)

    def one_week_change(self):
        self.change={}
        for d in self.data:
            self.c=d.get("Country/Region")
            self.now=int(d.get("Confirmed"))
            self.week_ago=int(d.get("Confirmed last week"))
            self.diff=self.now-self.week_ago
            if self.c in self.change:
                self.change[self.c]+=self.diff
            else:
                self.change[self.c]=self.diff
        print(self.change)

    def zero_new_deaths(self):
        self.most_d=[d.get("Country/Region") for d in self.data if float(d.get("New deaths"))==0]
        print(self.most_d)

    def max_who(self):
        self.who_c={}
        self.who=[d.get("WHO Region") for d in self.data]
        for w in self.who:
            if w in self.who_c:
                self.who_c[w]+=1
            else:
                self.who_c[w]=1
        for k,v in self.who_c.items():
            if v==max(v for v in self.who_c.values()):
                print(k)

    def max_new_caugth(self):
        self.most_d=[d.get("Country/Region") for d in self.data if float(d.get("New cases"))==max(float(d.get("New cases")) for d in self.data)]
        print(self.most_d)


covid_instance = Covid()
#covid_instance.most_affected()
#covid_instance.most_deaths()
#covid_instance.total_deaths()
#covid_instance.max_death_by_100()
#covid_instance.most_active()
#covid_instance.most_recovered()
#covid_instance.lowest_recovery_rate()
#covid_instance.max_recovered_by_100()
#covid_instance.max_death_by_recovered()
#covid_instance.most_affected_who()
#covid_instance.most_deaths_who()
#covid_instance.one_week_change()
#covid_instance.zero_new_deaths()
#covid_instance.max_who()
covid_instance.max_new_caugth()