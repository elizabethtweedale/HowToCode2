animals = ["badger","buffalo","bear"]
with open("newAnimals-2.txt", mode="w",encoding="utf-8") as myFile:
    for animal in animals:
        myFile.write(animal+"\n")
