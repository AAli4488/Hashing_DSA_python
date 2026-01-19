
# Count number of subarrays with sum exactly equal to K

arr = list(map(int, input("Enter array elements: ").split()))
K = int(input("Enter value of K: "))

prefix_sum = 0
count = 0
prefix_map = {0: 1}  # very important initialization

for num in arr:
    prefix_sum += num

    # Check if required prefix exists
    if prefix_sum - K in prefix_map:
        count += prefix_map[prefix_sum - K]

    # Store prefix sum frequency
    prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

print("Number of subarrays with sum", K, ":", count)
