
def bubbleSort(unsorted):
    noSwaps = True
    while noSwaps:
        noSwaps = False
        for item in range(1,len(unsorted)-1):
            if unsorted[item] > unsorted[item+1]:
                temp = unsorted[item+1]
                unsorted[item+1] = unsorted[item]
                unsorted[item] = temp
                noSwaps = True


with open("studentsUnsorted.txt",mode="r",encoding="utf-8") as myFile:
    students = myFile.read().splitlines()

bubbleSort(students)

with open("studentsSorted.txt",mode="w",encoding="utf-8") as myFile:
    for student in students:
        myFile.write(student+"\n")
