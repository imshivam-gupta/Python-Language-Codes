# Write a program to find the factorial of a number.
# Factorial of n is:
# n! = n * (n-1) * (n-2) * (n-3)....* 1
# Output the factorial of 'n'. If it does not exist, output 'Error'.
# Input Format :
# The only line of input contains a single integer.
# Output Format :
# The only line of output prints the Factorial of the number or "Error" if it doesn't exist.
# Constraints:
# -10 <= n <= 12
# Sample Input 1 :
# 5
# Sample Output 1 :
# 120
# Explanation Of Sample Input 1:
# 5!=5*4*3*2*1=120
# Sample Input 2 :
# 0
# Sample Output 2 :
# 1
# Explanation Of Sample Input 2:
# Its a fact that 0!=1
# Sample Input 3 :
# -2
# Sample Output 3 :
# Error
# Explanation Of Sample Input 3:
# It's a fact that we can't find the factorial of a negative number.


def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

a=int(input())
if(a<0):
    print("Error")
else:
	print(factorial(a))





