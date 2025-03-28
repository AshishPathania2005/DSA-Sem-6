# class NumMatrix(object):

#     def __init__(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         """
#         if not matrix or not matrix[0]:
#             return
        
#         self.rows, self.cols = len(matrix), len(matrix[0])
#         self.prefix_sum = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        
#         # Compute the prefix sum matrix
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 self.prefix_sum[i + 1][j + 1] = (
#                     matrix[i][j]
#                     + self.prefix_sum[i][j + 1]  # Left
#                     + self.prefix_sum[i + 1][j]  # Top
#                     - self.prefix_sum[i][j]  # Overlapping region
#                 )

#     def sumRegion(self, row1, col1, row2, col2):
#         """
#         :type row1: int
#         :type col1: int
#         :type row2: int
#         :type col2: int
#         :rtype: int
#         """
#         return (
#             self.prefix_sum[row2 + 1][col2 + 1]
#             - self.prefix_sum[row1][col2 + 1]
#             - self.prefix_sum[row2 + 1][col1]
#             + self.prefix_sum[row1][col1]
#         )

# # Example usage:
# matrix = [
#     [3, 0, 1, 4, 2],
#     [5, 6, 3, 2, 1],
#     [1, 2, 0, 1, 5],
#     [4, 1, 0, 1, 7],
#     [1, 0, 3, 0, 5]
# ]
# obj = NumMatrix(matrix)
# print(obj.sumRegion(2, 1, 4, 3))  # Output: 8



def RangeSumQuary(arr, queries):
    if arr == []:
        return []
    queries_sum = []
    for query in queries:
        sum = 0
        for i in range(query[0], query[1] + 1):
            sum += arr[i]
        queries_sum.append(sum)
        return queries_sum

print(RangeSumQuary([1, 2, 3, 4, 5], [[1, 2], [0, 3]]))





