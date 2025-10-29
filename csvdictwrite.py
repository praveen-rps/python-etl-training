import csv

data =[
    {"id":1, "name":"John Doe", "age":28, "email":"doe@gmail.com"},
    {"id":2, "name":"Jane Smith", "age":34, "email":"smith@gmail.com"},
    {"id":3, "name":"Charlie ", "age":29, "email":"charlie@gmail.com"},
    {"id":4, "name":"Daniel", "age":33, "email":"daniel@gmail.com"}
]

with open('d:/RPS/meghasree/practice/kyndryldata_dict.csv','w', newline='') as fp:
    filednames = ['id', 'name', 'age', 'email']
    csvwriter = csv.DictWriter(fp, fieldnames=filednames)
    csvwriter.writeheader()
    csvwriter.writerows(data)
    print("Data written to CSV file successfully.")