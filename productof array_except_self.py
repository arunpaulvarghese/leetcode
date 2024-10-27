# To find the product of an array except for itself

def productExceptSelf(nums):
    product = [1] * len(nums)
    for i in range(1, len(nums)):
        product[i] = product[i-1] * nums[i-1]

    right = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        product[i] = product[i] * right
        right = right * nums[i]

    return product


n = [2,3,4,5,6]
print(productExceptSelf(n))
