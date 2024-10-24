# search insertion position using the binary search
def insertionPosition(nums,number):
    last = len(nums) - 1
    first = 0
    while first < last:
        mid = (first + last) // 2
        if nums[mid] < number:
            first = mid + 1
        elif nums[mid] > number:
            last = mid - 1
        else:
            return mid
    return first



n = [3,5,3,6,6,1,2,8]
w = 1
print(insertionPosition(n,w))

