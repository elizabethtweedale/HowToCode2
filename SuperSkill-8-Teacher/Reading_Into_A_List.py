with open("B-Animals.txt", mode="r", encoding="utf-8") as myFile:
    animals = myFile.read().splitlines()
print(animals)
