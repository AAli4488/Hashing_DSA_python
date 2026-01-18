Pair With Given Sum
pair_with_given_sum.py
Question
Given an array and a target sum, check if any pair exists whose sum equals the target.
Input:
Array = [8, 7, 2, 5, 3, 1]
Target = 10

Output:
Pair found
arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target sum: "))

seen = set()
found = False

for num in arr:
    if target - num in seen:
        found = True
        break
    seen.add(num)

if found:
    print("Pair found")
else:
    print("Pair not found")
