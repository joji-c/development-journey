"""
step1: sort array
step2: set low=>0 upp=> array len
step3: iterate low<=upp
        step4: calculate mid => (low+upp)//2
        case1:
        search_element=arr[mid]
        case2:
        SE<arr[mid] (element in left side) upp=>mid-1
        case3:
        SE>arr[mid] (element in right side) upp=>mid+1
"""
class BinarySearch:
    def solution(self,arr,element):
        arr.sort()
        low = 0
        upp = len(arr)-1
        is_present = False
        while(low<=upp):
            mid = (low+upp)//2
            if arr[mid]==element:
                is_present = True
                break
            elif element<arr[mid]:
                upp = mid -1
            elif element>arr[mid]:
                low = mid + 1
        print(is_present)
bs_instance = BinarySearch()
arr = [10,11,12,13,14,15,16,17]
element = 16
bs_instance.solution(arr,element)