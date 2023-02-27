from random import choice

user_input = 0

print("Welcome to the Silly Sentence Generator!")
print("\nMenu:")
print("1. Generate a silly sentence")
print("2. Add a word to the action list")
print("3. Add a word to the animal list")
print("4. Add a word to the name list")
print("5. Add a word to the place list")

user_input = int(input("Enter a number: "))

if user_input == 1:
    actionF = open('random_sentence_genorator/action.txt')
    action = [line.strip() for line in actionF].pop()
    actionF.close()

    animalF = open('random_sentence_genorator/animal.txt')
    animal = [line.strip() for line in animalF]
    animalF.close()

    nameF = open('random_sentence_genorator/name.txt')
    name = [line.strip() for line in nameF]
    nameF.close()

    placeF = open('random_sentence_genorator/place.txt')
    place = [line.strip() for line in placeF]
    placeF.close()

    random_action = choice(action)
    random_animal = choice(animal)
    random_name = choice(name)
    random_place = choice(place)

    print(f"{random_name} is {random_action} with a {random_animal} in {random_place}.")


elif user_input == 2:
    with open('random_sentence_genorator/action.txt', 'r') as actionF:
        new_action = input("Enter a new action: ")
        while new_action.lower() in [line.strip() for line in actionF]:
            print("That word is already in the list.")
            new_action = input("Enter a new action: ")
    with open('random_sentence_genorator/action.txt', 'a') as actionF:
        actionF.write(new_action + "\n")