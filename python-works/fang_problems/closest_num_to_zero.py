class ClosestNumberToZero:
    def solution(self,*arr):
        closest_number=arr[0]
        for num in arr:
            if abs(num) < abs(closest_number):
                closest_number=num
        if closest_number<0 and abs(closest_number) in arr:
            return abs(closest_number)
        else:
            return closest_number

"""class ClosestNumberToZero:
    def solution(self,*arr):
        closest_number=0
        number={num:abs(num-closest_number) for num in arr}
        cl=[k for k,v in number.items() if v==min(number.values())]
        return max(cl)"""
    
cls_instance=ClosestNumberToZero()
print(cls_instance.solution(-4,-2,1,3,5))
