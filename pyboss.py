import csv

with open("employee_data.csv", "r") as f:
    data = csv.csv_reader(f)

    header = next(data)

    count = 0
    for d in data:
        count += 1
    print(count)