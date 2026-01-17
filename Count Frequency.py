Count Frequency of Elements
📄 frequency_count.py
🧠 Question
Given an array, count how many times each element appears.
Input:
1 2 1 3 2 1

Output:
1 -> 3
2 -> 2
3 -> 1
arr = list(map(int, input("Enter elements: ").split()))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for key in freq:
    print(key, "->", freq[key])
