
def quickSort(lists, low, high):
    if(low < high):
        p = partition(lists, low, high)
        quickSort(lists, low, p)
        quickSort(lists, p + 1, high)


def partition(lists, low, high):
    pivot = lists[low]
    lower = low - 1
    higher = high + 1
    while(lower < higher):
        lower += 1
        while(lists[lower] < pivot):
            lower += 1
        higher -= 1
        while(lists[higher] > pivot):
            higher -= 1
        if (lower < higher):
            temp = lists[lower]
            lists[lower] = lists[higher]
            lists[higher] = temp
    return higher


file = open(
    r"problems\p022_names.txt", "r")
list = file.readline()
list = list.replace('"', '')
list = list.split(",")
quickSort(list, 0, len(list) - 1)

totalScore = 0
nameIndex = 1
for name in list:
    sumOfNames = 0
    for i in name:
        sumOfNames += ord(i) - 64
    if(nameIndex <= 938):
        print(str(sumOfNames) + " " + name)
    totalScore += (sumOfNames) * nameIndex
    nameIndex += 1

print(totalScore)
