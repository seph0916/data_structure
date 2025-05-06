n = int(input())
arr = list(map(int, input().split()))

def doubble_sort(num, ls):
    for i in range(num):
        for j in range(num - 1 - i):
            if ls[j] > ls[j+ 1]:
                data = ls[j]
                ls[j] = ls[j + 1]
                ls[j+1] = data
    return ls
sorted_arr = doubble_sort(n, arr)
for k in sorted_arr:
    print(k, end=" ")