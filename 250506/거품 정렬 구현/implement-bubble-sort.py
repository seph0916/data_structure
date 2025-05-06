n = int(input())
arr = list(map(int, input().split()))

def bubble_sort(num, ls):
    for i in range(num):
        for j in range(num - 1 - i):
            if ls[j] > ls[j + 1]:  # ✅ ls로 비교
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls

sorted_arr = bubble_sort(n, arr)

for d in sorted_arr:
    print(d, end=" ")