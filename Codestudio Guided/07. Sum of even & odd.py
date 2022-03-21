# Problem Statement
# Write a program to input an integer N and print the sum of all its even digits and all its odd digits separately.
# Digits Mean Numbers, Not The Places! If The Given Integer Is "13245", Even Digits Are 2 & 4, And Odd Digits Are 1, 3 & 5.
# Input Format :
#  The only line of input contains a single integer N.
# Output Format :
# Print first even sum and then odd sum separated by space.
# Constraints
# 0 <= N <= 10^8
# Sample Input 1:
# 1234
# Sample Output 1:
# 6 4
# Sample Input 2:
# 552245
# Sample Output 2:
# 8 15
# Explanation For Sample Input 2:
# For the given input, the even digits are 2, 2, and 4, and if we take the sum of these digits, it will come out to be 8(2 + 2 + 4), and 
# similarly, if we look at the odd digits, they are, 5, 5 and 5 which makes a sum of 15(5 + 5 + 5). Hence the answer would be, 8(evenSum) 
# <single space> 15(oddSum)


a=int(input())
b=0
c=0
while(a>0):
    d=a%10
    if(d%2==0):
        b+=d
    else:
        c+=d
    a=int(a/10)
print(b,c)    



























