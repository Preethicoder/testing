

fileobj = open("grades.csv","r")
data = fileobj.read()
print(data)
fileobj.close()
with open("grades.csv","w") as fileobj1:
    fileobj1.write(data)