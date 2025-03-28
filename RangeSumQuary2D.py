# # class NumMatrix(object):

# #     def __init__(self, matrix):








# # #     matrix = [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]]

# #         rows = int(input("Enter number of rows: "))
# #         cols = int(input("Enter number of columns: "))

# #         matrix = []

# # # Taking input for the 2D list
# # print("Enter the elements row-wise:")
# # for i in range(rows):
# #     row = list(map(int, input().split()))  # Taking space-separated input for each row
# #     matrix.append(row)

# # # Printing the 2D list
# # print("The 2D array is:")
# # for row in matrix:
# #     print(*row) 



# # #         """
# # #         :type matrix: List[List[int]]
# # #         """
        

# # #     def sumRegion(self, row1, col1, row2, col2):
# # #         """
# # #         :type row1: int
# # #         :type col1: int
# # #         :type row2: int
# # #         :type col2: int
# # #         :rtype: int
# # #         """
        


# # # Your NumMatrix object will be instantiated and called as such:
# # # obj = NumMatrix(matrix)
# # # param_1 = obj.sumRegion(row1,col1,row2,col2)


# # # Taking input for the number of rows and columns


# class Solution(object):
#     def countOfSubstrings(self, word, k):
#         """
#         :type word: str
#         :type k: int
#         :rtype: int
#         """
#         vowels = {'a', 'e', 'i', 'o', 'u'}
#         count = 0
        
#         for start in range(len(word)):
#             vowel_set = set()
#             consonant_count = 0
            
#             for end in range(start, len(word)):
#                 if word[end] in vowels:
#                     vowel_set.add(word[end])
#                 else:
#                     consonant_count += 1
                
#                 if len(vowel_set) == 5 and consonant_count == k:
#                     count += 1
#                 elif consonant_count > k:
#                     break
        
#         return count



class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return
        
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        
        # Compute the prefix sum matrix
        for i in range(self.rows):
            for j in range(self.cols):
                self.prefix_sum[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.prefix_sum[i][j + 1]  # Left
                    + self.prefix_sum[i + 1][j]  # Top
                    - self.prefix_sum[i][j]  # Overlapping region
                )

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (
            self.prefix_sum[row2 + 1][col2 + 1]
            - self.prefix_sum[row1][col2 + 1]
            - self.prefix_sum[row2 + 1][col1]
            + self.prefix_sum[row1][col1]
        )

# Example usage:
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))  # Output: 8