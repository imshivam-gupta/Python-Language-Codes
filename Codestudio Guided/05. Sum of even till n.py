# Problem Statement
# Given a number N, print sum of all even numbers from 1 to N.
# Input Format :
# The only line of input contains an integer, N.
# Output Format :
# The only line of output prints the sum of all even numbers from 1 to N.
# Constraints :
#  1 <= N <= 10ˆ4 
# Sample Input 1 :
#  6
# Sample Output 1 :
# 12
# Explanation Of Sample Input 1:
# The even numbers from 1 to 6 are: 2, 4, 6, So adding these 3 numbers give a sum of 12.

n=int(input())
a=0
for i in range(2,n+1,2):  
    a+=i
print(a)

























