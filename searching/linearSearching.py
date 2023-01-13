people = ["Domey K", "Oscarrr", "Jakee", "Crumbs", "Davers", "Jebewok", "Conrr"]

searchName = input("Search name ")
for name in people:
    if searchName == name:
        print(f"{searchName} was found in position {people.index(name)}")
        break