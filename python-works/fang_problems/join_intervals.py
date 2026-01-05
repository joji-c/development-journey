class Intervals:
    def solution(self,lis):
        merged=[]
        merged.append(lis[0])
        for l in lis:
            if merged[-1][1]>=l[0]:
                merged[-1][1]=l[1]
            else:
                merged.append(l)
        return merged
cls_instance=Intervals()
print(cls_instance.solution([[1,3],[2,6],[8,10],[15,18]]))
