import csv
class Amasales:
    def __init__(self):
        file_path="python-works\\file_works\\amaz_sales\\amazon_sales_2025_INR_cleaned.csv"
        fr=open(file_path,'r',encoding='utf-8')
        read=csv.DictReader(fr)
        self.data=[r for r in read]
        
    def overall_avg(self):
        self.avg=[]
        self.sum=0
        self.count=0
        for d in self.data:
            self.met1=float(d.get('Metric1').replace('','0'))
            self.met2=float(d.get('Metric2').replace('','0'))
            self.met3=float(d.get('Metric3').replace('','0'))
            self.met4=float(d.get('Metric4').replace('','0'))
            if d.get("\ufeffReport_Section")=='AVERAGE_ORDER_VALUE':
                self.sum=self.met1+self.met2+self.met3+self.met4
        print(round(self.sum/4,2))

    def max_met1_pro(self):
        self.m1=[]
        for d in self.data:
            self.met1=float(d.get('Metric1').replace('','0'))
            if d.get("\ufeffReport_Section")=='CATEGORY_PERFORMANCE':
                self.m1.append(self.met1)
        self.an=[d.get('Dimension') for d in self.data if float(d.get('Metric1').replace('','0'))==max(self.m1)]
        print(self.an)

    def min_met1_pro(self):
        self.me1=[]
        for d in self.data:
            self.met1=float(d.get('Metric1').replace('','0'))
            if d.get("\ufeffReport_Section")=='CATEGORY_PERFORMANCE':
                self.me1.append(self.met1)
        self.ns=[d.get('Dimension') for d in self.data if float(d.get('Metric1').replace('','0'))==min(self.me1)]
        print(self.ns)

    def elec_met2(self):
        self.m2=[]
        for d in self.data:
            self.met2=float(d.get('Metric2').replace('','0'))
            if d.get("\ufeffReport_Section")=='PRODUCT_QUANTITY_DISTRIBUTION' and d.get('Dimension')=='Electronics':
                print(self.met2)
            
    def max_met2_pro(self):
        self.m2=[]
        for d in self.data:
            self.met2=float(d.get('Metric2').replace('','0'))
            if d.get("\ufeffReport_Section")=='CATEGORY_PERFORMANCE':
                self.m2.append(self.met2)
        self.an=[d.get('Dimension') for d in self.data if float(d.get('Metric2').replace('','0'))==max(self.m2)]
        print(self.an)

instance=Amasales()
#instance.overall_avg()
#instance.max_met1_pro()
#instance.min_met1_pro()
#instance.elec_met2()
#instance.max_met2_pro()
