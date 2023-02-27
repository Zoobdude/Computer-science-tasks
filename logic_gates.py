a = input("Enter a value of 1 or 0 for a ")
b = int(input("Enter a value of 1 or 0 for b "))

def andGate(a, b):
    if a == 1 and b == 1:
        print("a AND b = 1")
    else:
        print("a AND b = 0")

def xorGate(a, b):
    if a != b:
        print("a XOR b = 1")
    else:
        print("a XOR b = 0")


def notGate(a, b):
    if a == 1:
        print("a NOT = 0")
    else:
        print("a NOT = 1")

def orGate(a, b):
    if a == 1 or b == 1:
        print("A OR B = 1")
    else:
        print("A OR B = 0")

selectedGate = ""
selectedGate = input("Which gate would you like to use? \n 1. AND \n 2. XOR \n 3. NOT \n 4. OR \n ____ \n")

if selectedGate == "1":
    andGate(a, b)
if selectedGate == "2":
    xorGate(a, b)
if selectedGate == "3":
    notGate(a, b)
if selectedGate == "4":
    orGate(a, b)