# Write a function to print all divisors of a number.
# Divisors Are The Numbers That Divide The Number Entirely And Leaves No Remainder.
# Input Format :
# The only line of input contains a natural number N.
# Output Format :
# The only line of the output prints the Space Separated divisors of N.
# Constraints :
# 1 <= N <= 10ˆ3 
# Sample Input 1 :
# 10
# Sample Output 1 :
# 1 2 5 10
# Explanation Of Sample Input 1:
# The divisors of 10 are 1,2,5,10.


def printDivisors(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i,end=" ")

n = int(input())
printDivisors(n)

