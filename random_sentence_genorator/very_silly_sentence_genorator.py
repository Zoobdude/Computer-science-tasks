#random sentence generator
from random import choice
print(f"{(choice([line.strip() for line in open('name.txt')]))} is {(choice([line.strip() for line in open('action')]))} with a {(choice([line.strip() for line in open('animal.txt')]))} in {choice([line.strip() for line in open('place.txt')])}.")