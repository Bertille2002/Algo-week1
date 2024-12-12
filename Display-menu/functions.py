import csv

# menu display options
def display_menu():
    print("\nInteractive Menu:")
    print("1. View products only")
    print("2. Add a new product")
    print("3. Delete a product")
    print("4. Search for a specific product")
    print("5. Close file")
    option = input("Enter your choice (1-5): ")
    return option

# view products
def view_names(produits) :
  with open('produits.csv', 'r') as file :
    reader = csv.DictReader(file)
    print("List of products : ")
    for row in reader : 
      print(row['P_name'])

# add new product
def new_product(produits) :
  new_row = input("Enter a new row in the format : ID,P_name,P_quatity,P_price (in $/Kg),expiration_date")
  with open('produits.csv', 'a', newline='') as file :
    writer = csv.writer(file)
    writer.writerow(new_row)
  print("New product added successfully.")
  with open('produits.csv', 'r', newline='') as file :
    content = file.read()
    print(content)

# delete product row
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

# binary search
def binary_search(produits) :
    product_name = input("Enter product name for search : ")
    try :
        with open('produits.csv', 'r') as file :
            reader = csv.DictReader(file)
            rows = sorted(reader, key=lambda row: row['P_name'].lower())
        low, high = 0, len(rows) - 1
        while low <= high :
            mid = (low + high) // 2
            mid_name = rows[mid]['P_name'].lower()
            if mid_name == product_name.lower() :
                return rows[mid]
            elif mid_name < product_name.lower() :
                low = mid + 1
            else :
                high = mid - 1
        return None 
    except FileNotFoundError :
        print(f"Error : {produits} not found")
        return None
    except KeyError :
        print("Error : column P_name was not found")
