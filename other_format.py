with open("baseball.jpg","rb") as fileobj:
    data = fileobj.read()
    #print(data)
with open("baseball-copy.jpg","wb") as fileobj1:
    fileobj1.write(data)

with open("sample.mp3","rb") as fileobj2:
    data = fileobj2.read()
    #print(data)

with open("sample-twice.mp3","wb") as fileobj3:
    fileobj3.write(data)
    fileobj3.write(data)

with open("baseball-part.jpg","wb") as fileobj4:
    for index,line in enumerate(data):
        if index <= 30000:
            fileobj4.write(bytes(line))