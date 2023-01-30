#Create a ordered list of names
NAMES = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie", "Gina", "Hannah", "Isla", "Jack", "Katie", "Liam", "Mia", "Noah", "Olivia", "Paul", "Quinn", "Rory", "Samantha", "Toby", "Uma", "Vince", "Wendy", "Xavier", "Yvonne", "Zach"]
print(NAMES[-1])

nameFound = False
frontPointer = 0
backPointer = len(NAMES) - 1
findName = input("Enter Name")
nameLocation = ord(findName[0])
print(nameLocation)

while nameFound == False and frontPointer != NAMES[-1]:
    midPointOfList = backPointer // 2
    midPointWord = NAMES[midPointOfList]
    midPointNumber = ord(midPointWord[0])
    if midPointNumber > nameLocation:
        backPointer = midPointNumber
    elif midPointNumber < nameLocation:
         
