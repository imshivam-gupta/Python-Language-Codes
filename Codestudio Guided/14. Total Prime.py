# Write a program to find the total number of a primes number in a given interval.
# Given two integers S and E, count all primes between S and E.
# Input Format :
# The only line of input contains two integers S and E separated by a single space.
# Output Format :
# The only line of the output prints the total number of primes.
# Constraints
# 1 <= N <= 100
# Sample Input 1 :
# 2 10
# Sample Output 1 :
# 4
# Explanation Of Sample Input 1:
# The prime numbers between 2 and 10
# are 2,3,5 and 7
# Sample Input 2 :
# 2 5
# Sample Output 2 :
# 3


def isprime(num):
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):   
        if num%n==0:
            return False    
    return True

def totalPrime(a,b):
    count=0
    
    if(a==b):
        if(isprime(a)):
            return 1
        
    if((b-a)==1):
        if(a==2):
            return 2
        elif(isprime(a) or isprime(b)):
            return 1
        
    for i in range(a,b):
        if(i==2):
            count+=1
        else:
            prime=True; 
            for j in range(2,i):
                if(i%j==0):
                    prime=False
                    break
            if(prime):
                count+=1
                
    if(isprime(b)):
        return count+1
    
    return count
            
         	
      

    
#Taking S and E space seperated input.
S,E = map(int,input().split(' '))
print(totalPrime(S,E))


