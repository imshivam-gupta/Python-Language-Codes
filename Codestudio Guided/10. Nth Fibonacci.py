# You are given an integer ‘N’, your task is to find and return the N’th Fibonacci number using matrix exponentiation.
# Since the answer can be very large, return the answer modulo 10^9 +7.
# Fibonacci Number Is Calculated Using The Following Formula:
# F(n) = F(n-1) + F(n-2), 
# Where, F(1) = F(2) = 1.
# For Example:
# For ‘N’ = 5, the output will be 5.
# Input Format:
# The first line contains a single integer ‘T’ denoting the number of test cases to be run. Then the test cases follow.
# The first line of each test case contains a single integer ‘N’, representing the integer for which we have to find its equivalent Fibonacci number.
# Output Format:
# For each test case, print a single integer representing the N’th Fibonacci number.
# Return answer modulo 10^9 + 7.
# Output for each test case will be printed in a separate line.
# Note:
# You are not required to print anything; it has already been taken care of. Just implement the function.
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 10^9
# Time Limit: 1 sec.
# Follow Up:
# Can you solve it in Time Complexity better than O(N)?
# Sample Input 1:
# 2
# 10
# 7
# Sample Output 1:
# 55
# 13
# Explanation For Sample Output 1:
# For the first test case, the 10th Fibonacci number is 55.
# For the second test case, the 7th Fibonacci number is 13.
# Sample Input 2:
# 2
# 1
# 3
# Sample Output 2:
# 1
# 2




def fibonacciNumber(n):
    
    mod = int(1e9 + 7)

    # Base Case
    if (n <= 1):
        return n
    
    # Recursive call
    return (fibonacciNumber(n - 1) + fibonacciNumber(n - 2)) % mod
