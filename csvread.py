import csv

with open('d:/RPS/meghasree/practice/training.csv', mode='r') as fp:
    csvreader = csv.reader(fp)
    csvreader.__next__()  # Skip header row if present
    #csvreader.__next__() 
    for row in csvreader:
        print(row[1], " ", row[2], " ", row[3])