""" linear search: searching elements one by one for given value"""
class LinearSearching:
    def solution(self,arr,num):
        is_num=False
        for i in range(len(arr)):
            if arr[i]==num:
                is_num=True
                break
        print(is_num)
ls_instance = LinearSearching()
arr=[10,11,12,13,14,15,16,17,18]
ls_instance.solution([10,11,12,13,14,15,16,17,18],18)