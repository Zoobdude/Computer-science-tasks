allCharacters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

inputText = input("Enter the text to be encrypted: ")
key = int(input("Enter the key: "))
outputText = ""


for character in inputText:
    positionInAlphabet = allCharacters.index(character)
    newPosition = positionInAlphabet + key
    if newPosition > len(allCharacters):
        newPosition = newPosition - len(allCharacters)
    outputText += allCharacters[newPosition]

print(outputText)