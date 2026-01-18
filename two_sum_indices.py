Two Sum (Return Indices)
two_sum_indices.py
 Question
Return the indices of two numbers such that they add up to the target.
Input:
Array = [2, 7, 11, 15]
Target = 9

Output:
[0, 1]
arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))

index_map = {}

for i, num in enumerate(arr):
    if target - num in index_map:
        print("Indices:", index_map[target - num], i)
        break
    index_map[num] = i
