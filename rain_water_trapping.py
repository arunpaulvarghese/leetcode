def rainWaterTrapping(nums):
    volume = 0
    i = 0
    j = len(nums) - 1
    lmax = nums[0]
    rmax = nums[-1]

    while i < j:
        if lmax < nums[i]: # the value of i got incremented so both lmax and num[i] change at 2nd iteration
            lmax = nums[i]
        if rmax < nums[j]:   # the value of j got incremented so both rmax and num[j] changed at the coming iteration
            rmax = nums[j]

        if lmax < rmax:
            volume += lmax - nums[i]
            i +=1
        else:
            volume += rmax - nums[j]
            j -=1
    return volume

nu = [0,2,4,1,0,4,7,2,1,2,0,1]
print(rainWaterTrapping(nu))
