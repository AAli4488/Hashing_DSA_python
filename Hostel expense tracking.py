# Situation: Hostel expense tracking
# Check if any continuous days result in zero net expense

expenses = list(map(int, input("Enter daily expenses: ").split()))

prefix_sum = 0
seen = set()
exists = False

for amount in expenses:
    prefix_sum += amount

    # If prefix sum becomes zero or repeats
    if prefix_sum == 0 or prefix_sum in seen:
        exists = True
        break

    seen.add(prefix_sum)

if exists:
    print("Yes, zero-sum subarray exists")
else:
    print("No zero-sum subarray exists")
