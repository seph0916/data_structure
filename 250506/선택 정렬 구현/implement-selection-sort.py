n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(n):
    min = i
    for j in range(i+1, n, 1):
        if arr[min] > arr[j]:
            min = j
    data = arr[i]
    arr[i] = arr[min]
    arr[min] = data

for d in arr:
    print(d, end=" ")