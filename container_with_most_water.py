def waterContainer(height):
    max_area = 0
    l = 0
    r = len(height) -1
    while l < r:
        area = (r-l) * min(height[l], height[r])
        max_area = max(area,max_area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area


h = [4,5,2,7,4,8,4]
print(waterContainer(h))

