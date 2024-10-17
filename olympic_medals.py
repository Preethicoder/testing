with open('olympic-medals.csv',"r") as fileobj:
    data =  fileobj.read().splitlines()
    print(data)
    for index, line in enumerate(data):
        if index != 0:
            if ' China"' in line:
                Country = line.split(',')[0] + line.split(',')[1]
            else :
                Country = line.split(',')[0]
            with open(f"olympic-medals-{Country}.csv","w") as fileobj5:
                fileobj5.write(line)
   # print(data)

"""with open('olympic-medals-copy.csv',"w") as fileobj1:
    for line in data:
        fileobj1.write(f"{line}\n")

with open('olympic-medals-short.csv',"w") as fileobj2:
    for index, line in enumerate(data):
        if index == 10:
            break
        else:
            fileobj2.write(f"{line}\n")

with open('olympic-medals-5.csv',"w") as fileobj3:
    for index, line in enumerate(data):
        if index == 0:
            fileobj3.write(f"{line}\n")
        else:
            parts = line.split(',')

            if ' China"'in parts:
                gold = int(parts[2])  #
            else :
                gold = int(parts[1])
            if gold >= 5:
               fileobj3.write(f"{line}\n")

with open('olympic-medals-10.csv',"w") as fileobj4:
    for index, line in enumerate(data):
        if index == 0:
            fileobj4.write(f"{line}\n")
        else:
            parts = line.split(',')

            if ' China"' in parts:
                gold = int(parts[2])
                silver = int(parts[3])
                bronze = int(parts[4])
            else:
                gold = int(parts[1])
                silver = int(parts[2])
                bronze = int(parts[3])

            if (gold+silver+bronze) >= 10:
                fileobj4.write(f"{line}\n")"""




