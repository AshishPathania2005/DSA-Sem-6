def prefix_sum(arr):
    n = len(arr)
    sum = [0] * n 

    for i in range(n):
        sum[i] = 0  
        for j in range(i + 1):
            sum[i] += arr[j]

    return sum

arr = [1, 2, 3, 4, 5]
print (prefix_sum(arr))



















# # Example usage
# arr = [1, 2, 3, 4, 5]
# print("Original Array:", arr)
# print("Prefix Sum (Brute Force):", prefix_sum(arr))
