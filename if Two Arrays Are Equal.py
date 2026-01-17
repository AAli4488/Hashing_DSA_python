Check if Two Arrays Are Equal
📄 arrays_equal.py
🧠 Question
Check whether two arrays contain the same elements with same frequency.
Input:
Array1: 1 2 3 2
Array2: 2 1 2 3

Output:
Arrays are equal
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

freq1 = {}
freq2 = {}

for num in arr1:
    freq1[num] = freq1.get(num, 0) + 1

for num in arr2:
    freq2[num] = freq2.get(num, 0) + 1

if freq1 == freq2:
    print("Arrays are equal")
else:
    print("Arrays are not equal")
