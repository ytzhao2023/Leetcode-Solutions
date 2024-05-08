nums = [2, 3, 1, 2, 4, 3]
target = 4
subarrays = []
"""
for i in range(len(x)):
    for j in range(i+1, len(x)+1):
        subarray = x[i:j]
        subarrays.append(subarray)
print(subarrays)
"""
min_length = float("inf")
subarrays = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)+1):
        sum_subarray = 0
        subarray = nums[i:j]
        subarrays.append(subarray)
        for k in range(len(subarrays)):
            sum_subarray = sum(subarrays[k])
            if sum_subarray >= target:
                min_length = min(min_length, len(subarrays[k]))
print(min_length) if min_length != float('inf') else 0


