# Remove duplicates from a sorted array
def removeDuplicates(arr):
    lis = []
    for i in range(len(arr)):
        if arr[i] in lis:
            return print("duplicates present in the list")
            break
        else:
            lis.append(arr[i])
    return print("No duplicates present in the array")


a = [1,2,3,4,5,4]
print(removeDuplicates(a))

#############################################

def duplicates(num):
    replace = 1
    for i in range(1,len(num)):
        if num[i] != num[i-1]:
            num[replace] = num[i]
            replace += 1
    return num


a = [1,2,3,3,4,5]
print(duplicates(a))
