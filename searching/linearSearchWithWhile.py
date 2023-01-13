people = ["Domey K", "Oscarrr", "Jakee", "Crumbs", "Davers", "Jebewok", "Conrr"]

searchName = input("Searched name ")
foundName = False
currentRecordNum = 0

while foundName == False and currentRecordNum < len(people):
    if searchName == people[currentRecordNum]:
        foundName = True
        print(f"Name: {searchName} was found in position {currentRecordNum + 1}")
    else:
        currentRecordNum += 1

if foundName == False:
    print(f"Name: {searchName} was never found")