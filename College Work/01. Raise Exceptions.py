max=int(input("enter the maximum marks that can be obtained in a subject"))
total=0
for i in range(3):
    a=int(input("enter the marks obtained in subject {}    ".format(i+1)))
    if a>max:
        raise Exception("Invalid entry!! please try again")
        break
    else:
        total+=a
percentage=(total*100)/(3*max)
print("the overall percentage obtained from the 3 subjects is",percentage)
