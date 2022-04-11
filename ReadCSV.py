import csv

f = open('TSP.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

A = []

for line in rdr:
    A.append((line[0],line[1]))
    print(line)
f.close()


print(A)