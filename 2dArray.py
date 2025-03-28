# # #  First row (Top Row)
# # # last column (right most)
# # # bottom row (last row)
# # # right most column

# # arr = [
# #     [[9], [4], [45]],
# #     [[1], [5], [7]],
# #     [[8], [4], [6]]
# # ]

# # # Transpose

# # for i in range(len(arr)):
# #     for j in range(len(arr[i])):
# #         if i == j:
# #             # print (arr(), arr[i])
# #             print(f"arr[{i}][{j}] = {arr[i][j]}")


# # # for i in range(len(arr)):  # Loop through rows
# # #     for j in range(len(arr[i])):  # Loop through columns
# # #         if i == j:  # If row index == column index (diagonal elements)
# # #             print(f"arr[{i}][{j}] = {arr[i][j]}")


# # # print(arr[0])
# # # print(arr[1])
# # # print(arr[1])


# # # column_0 = [row[0] for row in arr]
# # # column_1 = [row[1] for row in arr]
# # # column_2 = [row[2] for row in arr]

# # # print (column_0)
# # # print (column_1)
# # # print (column_2)


# # # for i in range(len(arr)):  # Loop through rows
# # #     for j in range(len(arr[i])):  # Loop through columns
# # #         print(f"arr[{i}][{j}] = {arr[i][j]}")




# class Solution(object):
#     def spiralOrder(self, matrix):
#         matrix = [
#     [[9], [4], [45]],
#     [[1], [5], [7]],
#     [[8], [4], [6]]
# ]
       
    
        
#         result = []
        
        
#         while left <= right and top <= bottom:
#             # Traverse from left to right
#             for i in range(left, right + 1):
#                 result.append(matrix[top][i])
#             top += 1
            
#             # Traverse from top to bottom
#             for i in range(top, bottom + 1):
#                 result.append(matrix[i][right])
#             right -= 1
            
#             if top <= bottom:
#                 # Traverse from right to left
#                 for i in range(right, left - 1, -1):
#                     result.append(matrix[bottom][i])
#                 bottom -= 1
            
#             if left <= right:
#                 # Traverse from bottom to top
#                 for i in range(bottom, top - 1, -1):
#                     result.append(matrix[i][left])
#                 left += 1
        
#         return result
# spiralOrder(self, matrix)

