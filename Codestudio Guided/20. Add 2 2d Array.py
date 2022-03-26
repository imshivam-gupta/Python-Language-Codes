def two_d_matrix(m, n): # define the function  
    Outp = []  # initially output matrix is empty  
    for i in range(m): # iterate to the end of rows  
        row = []  
        for j in range(n): # j iterate to the end of column  
            num = int(input(f "Enter the matrix [{0}][{j}]"))  
            row.append(num) # add the user element to the end of the row  
        Outp.append(row) # append the row to the output matrix  
    return Outp      
  
def sum(A, B): # define sum() function to add the matrix.  
    output = [] # initially, it is empty.  
    print("Sum of the matrix is :")  
    for i in range(len(A)): # no. of rows  
        row = []  
        for j in range(len(A[0])): # no. of columns  
              
            row.append(A[i][j] + B[i][j]) # add matrix A and B  
        output.append(row)  
    return output    # return the sum of both matrix  
  
m = int(input("Enter the value of m or Row\n")) # take the rows  
n = int(input("Enter the value of n or columns\n")) # take the columns  
  
print("Enter the First matrix ") # print the first matrix  
A = two_d_matrix(m, n) # call the matrix function  
print("display the first (A) matrix")  
print(A) # print the matrix  
  
print("Enter the Second (B) matrix ")  
B = two_d_matrix(m, n) # call the matrix function  
print("display the Second (B) matrix")  
print(B) # print the B matrix  
  
s= sum(A, B) # call the sum function  
print(s) # print the sum of A and B matrix.  
