Count Distinct Elements
📄 count_distinct.py
🧠 Question
Count the number of distinct elements in an array.
Input:
1 2 2 3 4 4

Output:
4
arr = list(map(int, input("Enter elements: ").split()))

distinct = set(arr)

print("Count of distinct elements:", len(distinct))
