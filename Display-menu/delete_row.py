### function to delete product row ###
import csv
def delete_product(produits, row_to_delete) :
  row_to_delete = input("Enter the row you wish to delete.")
  try :
    with open('produits.csv', 'r') as file : 
      reader = csv.DictReader(file)
      rows = [row for row in reader if row["P_name"] != row_to_delete]
    if len(rows) == 0 or (len(rows) == sum(1 for _ in open(produits)) - 1) :
      print(f"No row with Name = '{row_to_delete}' was found.")
      return
    with open('produits.csv', 'w', newline='') as file :
      fieldnames = reader.fieldnames
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(rows)
    print(f"The product : {row_to_delete} has been deleted.")

  except FileNotFoundError:
    print(f"Error: The file '{produits}' does not exist.")
  except KeyError:
    print(f"Error: The column 'P_name' does not exist in the file.")

delete_product('produits.csv', row_to_delete=row_to_delete)