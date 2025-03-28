# def recursive_sum(n):
#     if n == 1:
#         return 1
#     return n + recursive_sum(n - 1) 

# print(recursive_sum(5))  

# def factorial_number(n):
#     if (n == 1):
#         return 1
#     return n * factorial_number(n-1)
# n = int(input("Enter the number: "))

# print(factorial_number(n))


# public class RecursionExample {
#     public static int factorial(int n) {
#         if (n == 1)  // Base case
#             return 1;
#         return n * factorial(n - 1);  // Recursive case
#     }

#     public static void main(String[] args) {
#         System.out.println(factorial(5)); // Output: 120
#     }
# }

# def sum_of_digit(n):
#     if (n==0):
#         return 0
#     else (n)
        

# def sum_of_digit(num):
    
#     digits = [int(digit) for digit in str(num)]  # Convert to string, iterate, and convert back to int
    
#     print (sum_of_digit(234))
#     print(digits)
# def sum(num):
    
#     digits = [int(digit) for digit in str(num)]  # Convert to string, iterate, and convert back to int
#     print(digits)

# import math
# def sum_of_digit(num):
#     digits = [int(digit) for digit in str(num)]  # Convert number to list of digits
#     return math.prod(digits)  # Return sum of digits


# print(sum_of_digit(234))


# print subset

def subset(n):
    digits = [int(digit) for digit in str(n)]
    if n == 0:
        return 0
    else:
        return digits
    print (subset(234))
    

    # 2^n

    