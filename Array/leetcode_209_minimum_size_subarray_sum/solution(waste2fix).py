nums =[2, 3, 1, 2, 4, 3]
target = 100
min_length = float('inf')
sum_list = []
sum = 0
for i in range(len(nums)):
    sum += nums[i]
    sum_list.append(sum)

for i in range(len(nums)):
    for j in range(i+1, len(nums)+1):
        subarray = nums[i:j]
        if i == 0:
            sum_subarray = sum_list[j - 1]
        else:
            sum_subarray = sum_list[j - 1] - sum_list[i - 1]
        if sum_subarray >= target:
            min_length = min(min_length, len(subarray))
print(min_length) if min_length != float('inf') else 0