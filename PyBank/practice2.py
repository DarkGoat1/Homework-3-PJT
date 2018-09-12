list1 = [1, 2, 5, 6, 7, 8]


for x in range(0, 5):
    thing = int(list1[x+1]) - int(list1[x])
    print(thing)