count = 0
fname = input("Enter a file name: ")
fhand = open(fname)
for line in fhand:
    if line.startswith("From"):
        if line.startswith("From: "):
            continue
        else:
            count = count+1
            listz = line.split()
            print(listz[1])
print("There were",count,"lines in the file with from as the first word")
