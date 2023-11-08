nums = [2,7,11,15]
target = 9

break_check = False
for i in range(1, len(nums)):
    for j in range(i):
        if nums[i] + nums[j] == target:
            break_check = True
            print([i,j])
        break
    if break_check:
        break