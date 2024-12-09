### function to see product names ###
import csv 
def view_names(produits, P_name) :
  with open('produits.csv', 'r') as file :
    reader = csv.DictReader(file)
    print("List of products : ")
    for row in reader : 
      print(row[P_name])

view_names('produits.csv', 'P_name')