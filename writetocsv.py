import csv

data = [
    ['ID', 'Name', 'Age', 'Email'],
    [1, 'John Doe', 28, 'john@gmail.com'],
    [2, 'Jane Smith', 34, 'smith@gmail.com'],
    [3, 'Emily Davis', 22, 'emily@gmail.com'],
    [4, 'Michael Brown', 45, 'brown@gmail.com'],
    [5, 'Sarah Wilson', 31, 'sarah@gmail.com']
  ]

with open('d:/RPS/meghasree/practice/kyndryldata.csv','w', newline='') as fp:
    csvwriter = csv.writer(fp)
    csvwriter.writerows(data)
    print("Data written to CSV file successfully.")