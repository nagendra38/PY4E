fname = input("Enter the name of the file: ")
fhan = open(fname)
list1 = list()
for line in fhan:
    for word in line.split():
        if word in list1:
            continue
        else:
            list1.append(word)
list1.sort()
#list1 = list(dict.fromkeys(list1))
print(list1)
