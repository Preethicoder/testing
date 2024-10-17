from statistics import mean

with open("emotions.txt","r") as fileobj:
        words = fileobj.read().splitlines()
        value = []
        date_value = []

        for i in range(1,len(words)):
             date_val = words[i].split(",")[0]

             month,date,year = date_val.split("/")

             if (int(year)== 2016 and int(month)>= 6) or (int(month)<= 5 and int(year) == 2017):
                 value.append(float(words[i].split(",")[1]))
                 date_value.append(float(words[i].split(",")[5]))
        mean_SP = mean(value)
        print(mean_SP)
        max_interest =max(date_value)
        print(max_interest)














