First Non-Repeating Element
📄 first_non_repeating.py
🧠 Question
Find the first element that appears only once.
Input:
1 2 2 3 1 4

Output:
3
arr = list(map(int, input("Enter elements: ").split()))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for num in arr:
    if freq[num] == 1:
        print("First non-repeating element:", num)
        break
else:
    print("No non-repeating element")
