# # max product where product less then k

# arr = [10, 5, 2, 6]

# total_product = 0
# k = 100
# current_product = 0

# for i in len(arr):
#     current_product*= arr[i]




arr = [5,10,2,5]
k = int(input('Enter the k: '))

max_product = 0
current_product = 1

# Compute product of the first k elements
for i in range(k):
    current_product *= arr[i]

if current_product < 100:
    max_product = current_product

# Sliding window: Move one element at a time
for i in range(k, len(arr)):
    if arr[i - k] != 0:  # Avoid division by zero
        current_product = (current_product // arr[i - k]) * arr[i]
    else:
        # Recalculate the product from scratch if a zero was in the previous window
        current_product = 1
        for j in range(i - k + 1, i + 1):
            current_product *= arr[j]

    if current_product < 100:
        max_product = max(max_product, current_product)

print("Maximum product of", k, "consecutive elements (under 100):", max_product)













# arr = [2,1,5,1,3,2]
# # k = int (input ('Enter the k: '))
# max_sum = 0
# current_sum = 0

# for i in arr[]:
#     current_sum += arr[i]



# if (current_sum > max_sum):
#     max_sum = current_sum

# print(current_sum)






# arr = [2, 1, 5, 1, 3, 2]
# k = int(input('Enter the k: '))

# max_sum = 0
# current_sum = 0

# # Check if k is larger than the array length
# # if k > len(arr):
# #     print("Error: k should be less than or equal to the array length.")
# # else:
#     # Calculate sum of the first k elements
# for i in range(k):
#         current_sum += arr[i]

# max_sum = current_sum  # Initialize max_sum with the first window sum

#     # Sliding window: Move the window one element at a time
# for i in range(k, len(arr)):
#         current_sum += arr[i] - arr[i - k]  # Add new element, remove old one
#         max_sum = max(max_sum, current_sum)  # Update max_sum if needed

# print("Maximum sum of", k, "consecutive elements:", max_sum)









# # def sliding_window (max_sum, current_sum):
# #     max_sum = 0
# #     current_sum = 0
# #     return

# # for range in arr:
# #     if 






# # def check_length(str1, str2):
# #     return len(str1) == len(str2)