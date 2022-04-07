file = open('d:\VS Cpde\college codes\Project_19\input.txt','r')
f=open('d:\VS Cpde\college codes\Project_19\output.txt','w')
str=file.read()
for i in str:
    if(i.islower()):
        i=i.upper()
        f.write(i)
    elif(i.isupper()):
        i=i.lower()
        f.write(i)
    else:
        f.write(i)
f.close()
