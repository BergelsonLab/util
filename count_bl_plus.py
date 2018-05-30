import csv


file = "/Users/andrei/BLAB_DATA/all_basiclevel/all_basiclevel.csv"

df = []

with open(file, "rU") as input:
    reader = csv.reader(input)
    reader.next()
    for row in reader:
        df.append(row)


bl = [x[7] for x in df]

count = 0
for x in df:
    if "+" in x[7] and x[7][0].isupper() and x[10]=="06" and x[12] == "video":
        count += 1

print count
