Intersection of Two Arrays
intersection_arrays.py
Question
Find the common elements between two arrays.
Input:
Array1 = [1, 2, 2, 1]
Array2 = [2, 2]

Output:
[2]
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

set1 = set(arr1)
intersection = set()

for num in arr2:
    if num in set1:
        intersection.add(num)

print("Intersection:", list(intersection))
