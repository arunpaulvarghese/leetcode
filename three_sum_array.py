# Program to find the three elements in an array into zero
def threeSumArray(num):
    num.sort()
    answer = []
    for i in range(len(num)-2):
        if i > 0 and num[i] == num[i-1]:
            continue
        l = i + 1
        r = len(num) - 1
        while l < r:
            sum = num[l] + num[r] + num[i]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                triplet = [num[i], num[l], num[r]]
                answer.append(triplet)
                while l < r and num[l] == triplet[1]:
                    l +=1
                while l < r and num[r] == triplet[2]:
                    r -= 1
        return answer


n = [-1,-3,-5,3,5,6,9,2]
print(threeSumArray(n))
