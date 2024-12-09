## create csv file ###
import csv
from csv import writer

data = [
    [1,"pomme","5","18.2","12-05-24"],
    [2,"oeuf","9","43.1","27-12-24"],
    [3,"pasta","27","1.05","18-10-27"]
]

with open('produits.csv', 'w', newline='') as file :
    writer = csv.writer(file)
    field = ["ID","P_name", "P_quatity", "P_price (in $/Kg)", "expiration_date"]

    writer.writerow(field)
    writer.writerows(data)

file = open('produits.csv','r')
data = file.read()
print(data)
file.close()

# new_data = [4,"beer","67","29.95","18-01-25"]

# with open('produits.csv','a') as file :
#     file.writerow(new_data)

import csv

### create text file ###
path = 'Python/Python_cours/text.txt'

with open(path, 'w') as file :
    file.write('New file created \n')
    file.close()

### add text to text file ###
with open(path,'a') as file :
    file.write('this is a test \n')
    file.close()

### read file ###
with open(path,'r') as file :
    cont = file.read

print(cont)
file.close()

