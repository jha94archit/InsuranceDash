import csv
from core.models import Policy, Fuel, Vehicle_Segment, Customer_Income_Group, Customer_Region

file = open("dataset.csv")
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
print(Policy.objects.get.all())
file.close()
