# Write a program to find x to the power n (i.e., x^n). Take x and n from the user. You need to print the answer.
# Note: For this question, you can assume that 0 raised to the power of 0 is 1
# Input Format :
# The only line of input contains two integers x and n separated by a single space.
# Output Format :
# The only line of output prints the power of the number.
# Constraints:
# 0 <= x <= 8 
# 0 <= n <= 9
# Sample Input 1 :
#  3 4
# Sample Output 1 :
# 81
# Explanation Of Sample Input 1:
# 3^4=3*3*3*3=81
# Sample Input 2 :
#  2 5
# Sample Output 2 :
# 32
# Explanation Of Sample Input 2:
# 2^5=2*2*2*2*2=32

x, y = map(int, input().split())
print(x**y)
