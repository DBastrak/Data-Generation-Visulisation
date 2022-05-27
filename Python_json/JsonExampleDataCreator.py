import json
import random



def jsonPersonExample():
    firstM = ["Tim", "Kader", "Ben", "Ralph", "Wilson", "Dmitriy", "Ethan", "Ivan", "John", "Ali", "Oliver", "James", "Jack", "Alex", "Liam", "Elijah", "Henry", "Lucas", "Daniel"]
    firstFM = ["Genevieve", "Emma", "Emily", "Isobelle", "Ashlee", "Kira", "Juilia", "Olivia", "Chloe", "Amy", "Sophia", "Mia", "Elizabeth", "Zoe", "Gianna", "Aria", "Avery", "Layla"]
    LastName = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodrigues", "Martinez", "Lee", "Clark", "Walker",
                "Hernandez", "Lopez", "Thomas", "Taylor", "Anderson", "Moore", "Jackson", "Allen", "King", "Wright", "Scott", "Hill"]
    drinks = ["Juice", "Water", "Coffee", "Tea", "Soft drink"]
    people ={"Key":{"Name":{"FirstName":"Str","LastName":"Str"},"Sex":"Str","Age":"Int","hasVoted":"True/False","DrinkPreference":"Str"},
            "Data":{"People":[]}
            }
    for x in range(10000):
        gn = random.randrange(0,1)
        if gn == 0:
            firstName = firstM[random.randrange(0,18)]
            sex = "Male"
        else:
            firstName = firstFM[random.randrange(0,17)]
            sex = "Female"
        ln = random.randrange(0,24)
        lastName = LastName[ln]
        age = random.randrange(10,80)
        if age >= 18:
            voted = random.randrange(0,1)
            if voted == 1:
                vote = True
            else:
                vote = False
        else:
            vote = False
        drink = drinks[random.randrange(0,4)]
        people["Data"]["People"].append({"Name": {"FirstName":firstName, "LastName":lastName}, "Sex":sex, "Age":age, "hasVoted":vote, "DrinkPreference":drink})

    with open("examplePeople.json", "w") as js:
        json.dump(people, js)



def jsonRandomDateExample():
    minute = 0
    hour = 0
    day = 1
    month = 1
    year = 2020
    min = 10000
    max = 100000
    dictionary ={"Key":
                    {"Date":
                        {"Time":"Data"}
                    },
                "Data":{}
                }


    while True: #month cycle

        day = 1

        while True: #Day cycle
            
            date_ = f"{day}/{month}/{year}"
            print(date_)
            dictionary["Data"][date_] = {}
            hour = 0
            
            while True: #HourCycle

                minute = 0

                while True: #MinuteCycle
                    data = random.randrange(min,max)

                    if hour < 10 and minute < 10:
                        time_ = f"0{hour}:0{minute}"
                    elif hour < 10:
                        time_ = f"0{hour}:{minute}"
                    elif minute < 10:
                        time_ = f"{hour}:0{minute}"
                    else:
                        time_ = f"{hour}:{minute}"
                    dictionary["Data"][date_][time_] = data
                    minute += 1

                    if minute == 60:
                        break

                hour += 1
                if hour == 24:
                    break

            day += 1
            if day == 32:
                min += 1000
                max += 10000
                break
            elif day == 31 and month in [4, 6, 9, 11]:  
                min -= 1000
                max -= 10000
                break
            elif day == 30 and month == 2:
                break

        month += 1
        if month == 13:
            break      

    with open("exampleYearLong.json", "w") as js:
        json.dump(dictionary, js)
    
    
            


if __name__ == "__main__":
    jsonRandomDateExample()
    #jsonPersonExample()
