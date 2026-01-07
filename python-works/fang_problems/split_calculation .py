class splitwise:
    def solution(self):
        payment_summary={
            "hari":1200,
            "vipin":1400,
            "jhon":1000,
            "vishnu":0,
            "tom":120,
            "avinash":0,
            "jini":0,
            "asok":0
        }
        avg_amount = sum(payment_summary.values())/len(payment_summary)
        print(avg_amount)
        new_dict = {k:v-avg_amount for k,v in payment_summary.items()}
        print(new_dict)      
split_instance=splitwise()
split_instance.solution()
