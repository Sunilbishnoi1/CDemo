#lets implement binary search 
def binarySearch(arr,low,high,target):
    if low>high:
        return -1
    mid = (low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        high = mid-1
        return binarySearch(arr,low,high,target)
    else:
        return binarySearch(arr,mid+1,high,target)

arr = [1,2,4,5,6,7,8,9,15,17]
target = input("what do you want to search: ")
target = int(target)
result = binarySearch(arr,0,9,target)
print(f"this element is at {result} index of arrray")