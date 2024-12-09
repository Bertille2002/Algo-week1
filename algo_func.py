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

print("Option 1 : view products only")
print("Option 2 : add product")
print("Option 3 : delete product")
print("Option 4 : close file")

input = int(input("Enter one of the 4 options : "))

def function() :
    if input == 1 :
        with open('produits.csv','r') as file :
            cont = file.read
        print(file['P_name'])
    if input == 2 :
        new_data = input("Enter new data in csv format :")
        with open('produits.csv','a') as file_n :
            file_n.writerow(new_data)
            file_n.close()
    if input == 3 :
        chosen_row = int(input("Enter the ID number of the row you would like to delete : "))
        with open('produits.csv','a') as file_d :
            delete_row('produits.csv',chosen_row)
    if input == 4 :
        with open('produits.csv','r') as file :
            file.close()
    else :
        print("Error input invalid")