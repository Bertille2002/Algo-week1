### function to add new product to file ###
import csv
def new_product(produits) :
  new_row = input("Enter a new row in the format ")
  with open('produits.csv', 'a', newline='') as file :
    writer = csv.writer(file)
    writer.writerow(new_row)
  print("New product added successfully.")