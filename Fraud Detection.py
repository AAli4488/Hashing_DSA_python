
# Fraud Detection: Count subarrays with sum exactly K

transactions = list(map(int, input("Enter transactions: ").split()))
K = int(input("Enter target amount K: "))

prefix_sum = 0
count = 0
prefix_map = {0: 1}  # Important: handles subarrays starting at index 0

for amount in transactions:
    prefix_sum += amount

    # Check how many times (prefix_sum - K) occurred
    if prefix_sum - K in prefix_map:
        count += prefix_map[prefix_sum - K]

    # Store current prefix sum frequency
    prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

print("Suspicious transaction windows:", count)
