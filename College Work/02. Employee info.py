d={}
n=int(input("enter the number of employees"))
for i in range(1,n+1,1):
    nm=input("enter the name of the employee ")
    emp_code=input("enter the employee code ")
    sal=int(input("enter the employee's salary "))
    d[i]={'Name':nm,'Emp_Code':emp_code,'Salary':sal}
while(True):
    print("1.Accessing")
    print("2.Modifying")
    print("3.Exit")
    ch=int(input("enter your choice??...1/2/3"))
    if (ch==1):
        crt=input("enter the criteria by which you would like to access the details of the employee??...Name/Emp_Code/Salary")
        if (crt=='Name'):
            name=input("enter the name of the employee") 
            for k in range(1,n+1,1):
                if (d[k]['Name']==name):
                    print(d[k])
                    break
            else:
                print("Sorry!! No employee with the given name exists in our record")
        if (crt=='Emp_Code'):
            ec=input("enter the employee code")
            for l in range(1,n+1,1):
                if (d[l]['Emp_Code']==ec):
                    print(d[l])
                    break
            else:
                print("Sorry!! No employee with the given employee code exists in our record")
        if (crt=='Salary'):
            s=int(input("enter the salary of the employee"))
            for m in range(1,n+1,1):
                if (d[m]['Salary']==s):
                    print(d[m])
                    break
            else:
                print("Sorry!! No employee with the given salary exists in our record")
        else:
            print("Sorry!! Invalid input")
    if (ch==2):
        crt1=input("enter the criteria which you would like to modify??...Name/Emp_Code/Salary")
        if (crt1=='Name'):
            name=input("enter the previously inputted name of the employee")
            for k in range(1,n+1,1):
                if (d[k]['Name']==name):
                    nm1=input("enter the corrected/new name of the employee")
                    d[k]['Name']=nm1
                    print("the updated record is")
                    print(d[k])
                    break
            else:
                print("Sorry!! No employee with the given name exists in our record")
        if (crt1=='Emp_Code'):
            ec=input("enter the previous employee code")
            for l in range(1,n+1,1):
                if (d[l]['Emp_Code']==ec):
                    ec1=input("enter the corrected/new employee code of the employee")
                    d[l]['Emp_Code']=ec1
                    print("the updated record is")
                    print(d[l])
                    break
            else:
                print("Sorry!! No employee with the given employee code exists in our record")
        if (crt1=='Salary'):
            s=int(input("enter the salary of the employee"))
            for m in range(1,n+1,1):
                if (d[m]['Salary']==s):
                    s1=input("enter the corrected/new salary of the employee")
                    d[m]['Salary']=s1
                    print("the updated record is")
                    print(d[m])
                    break
            else:
                print("Sorry!! No employee with the given salary exists in our record")
        else:
            print("Sorry!! Invalid input")
    if (ch==3):
        break
    if (ch<1 and ch>3):
        print("Invalid input!! Please try again")


            
