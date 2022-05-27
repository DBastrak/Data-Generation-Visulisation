import json


def readJson() -> dict:

    with open("exampleYearLong.json", "r") as file:
        data = json.load(file)

    return data

def dayValid(day, month) -> []:
    if day == 32:
        day = 1
        month += 1
    elif day == 31 and month in [4, 6, 9, 11]:  
        day = 1
        month += 1
    elif day == 30 and month == 2:               
        day = 1
        month += 1
    return day, month

def averageDay(data, date):
    narrowedData = data["Data"][date]
    total = 0
    for key in narrowedData:
        total += narrowedData[key]
    
    avgDay = total/len(narrowedData)
    #print(avgDay)
    return avgDay

def averageWeek(data, startDate):
    narrowedData = data["Data"]
    copyDate = startDate
    first = copyDate.find("/")
    day = int(copyDate[:first])
    
    copyDate = copyDate[first+1:]
    second = copyDate.find("/")
    month = int(copyDate[:second])

    listOfDays = [startDate]
    for i in range(6):
        day += 1
        day, month = dayValid(day, month)

        listOfDays.append(f"{day}/{month}/{2020}")
    total = 0
    totalLen = 0
    for item in listOfDays:
        totalLen += len(narrowedData[item])
        for key in narrowedData[item]:
            total += narrowedData[item][key]
    
    print(total/totalLen)

def averageThroughTheWeek(data, startDate):
    narrowedData = data["Data"]
    copyDate = startDate
    first = copyDate.find("/")
    day = int(copyDate[:first])
    
    copyDate = copyDate[first+1:]
    second = copyDate.find("/")
    month = int(copyDate[:second])

    listOfDays = [startDate]
    for i in range(6):
        day += 1
        day, month = dayValid(day, month)

        listOfDays.append(f"{day}/{month}/{2020}")
    totalsAvg = []
    for item in listOfDays:
        totalsAvg.append(averageDay(data, item))
    
    print(totalsAvg)

def averageMonth():
    pass

def averageThreeMonth():
    pass

def averageSixMonth():
    pass

def averageYear():
    pass

if __name__ == "__main__":
    data = readJson()
    #averageDay(data, "1/1/2020")
    averageWeek(data, "28/2/2020")
    averageThroughTheWeek(data, "28/2/2020")