nums =[2, 3, 1, 2, 4, 3]
target = 7
min_length = float('inf')
for i in range(len(nums)):
    sum_subarray = 0
    for j in range(i, len(nums)):
        sum_subarray += nums[j]
        if sum_subarray >= target:
            min_length = min(min_length, j - i + 1)
            break
print(min_length) if min_length != float('inf') else 0       