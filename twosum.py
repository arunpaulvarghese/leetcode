# Two Sums
def twosums(target, nums):
    sceen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in sceen:
            n,m = [sceen[diff],i]
            return nums[n],nums[m]
        else:
            sceen[nums[i]] = i
rtarget = 5
n = [3,6,4,5,2]
print(twosums(rtarget,n))



