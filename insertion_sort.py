# insertion sort without swapping two variables
def insertionSort(numbers):
    for i in range(1, len(numbers)):
        j = i - 1
        key = numbers[i]
        while j >= 0 and key < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = key
    return numbers

num = [5,2,6,1,3,7]
print(insertionSort(num))
