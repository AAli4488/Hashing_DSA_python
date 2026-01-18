Subarray With Sum = 0
subarray_sum_zero.py
Question
Check if there exists a subarray with sum equal to 0.
Input:
Array = [4, 2, -3, 1, 6]

Output:
Subarray exists
arr = list(map(int, input("Enter array elements: ").split()))

prefix_sum = 0
seen = set()
exists = False

for num in arr:
    prefix_sum += num
    if prefix_sum == 0 or prefix_sum in seen:
        exists = True
        break
    seen.add(prefix_sum)

if exists:
    print("Subarray exists")
else:
    print("No such subarray")
