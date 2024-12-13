import csv

# menu display options
def display_menu():
    print("\nInteractive Menu:")
    print("1. View products only")
    print("2. Add a new product")
    print("3. Delete a product")
    print("4. Search for a specific product")
    print("5. Sort table")
    print("6. Close file")
    option = input("Enter your choice (1-5): ")
    return option

# view products
def view_names() :
  with open('produits.csv', 'r') as file :
    reader = csv.DictReader(file)
    print("List of products : ")
    for row in reader : 
      print(row['P_name'])

# add new product
def next_id() :
  with open('produits.csv','r',newline='') as file :
    reader = csv.reader(file)
    rows = list(reader)
    last_row = rows[-1]
    last_id = int(last_row[0])
    return last_id + 1

def new_product() :
  new_prod = input("Enter the name of a new product : ")
  new_quant = input("Enter its quantity : ")
  new_price = input("Enter its price (/kg) : ")
  new_expdate = input("Enter the expiration date (dd-mm-yy) : ")
  new_id = next_id()
  new_row = [new_id,new_prod,new_quant,new_price,new_expdate]
  with open('produits.csv', 'a', newline='') as file :
    writer = csv.writer(file)
    writer.writerow(new_row)
  print("New product added successfully.")
  with open('produits.csv', 'r', newline='') as file :
    content = file.read()
    print(content)

# delete product row
def delete_product() :
  row_to_delete = input("Enter the row you wish to delete.")
  try :
    with open('produits.csv', 'r') as file : 
      reader = csv.DictReader(file)
      rows = [row for row in reader if row["P_name"] != row_to_delete]
    with open('produits.csv','r') as file : 
      total_rows = sum(1 for _ in file)
    if len(rows) == 0 or len(rows) == total_rows - 1 :
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
def binary_search() :
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
              print(f"Product '{product_name}' found!")
              return rows[mid]
            elif mid_name < product_name.lower() :
                low = mid + 1
            else :
                high = mid - 1
        print(f"Product '{product_name}' not found.")
        return None 
    except FileNotFoundError :
        print(f"Error : {produits} not found")
        return None
    except KeyError :
        print("Error : column P_name was not found")

# quicksort quantity
def quicksort(produits, low, high) :
  try :
    with open('produits.csv','r') as file :
      reader = csv.reader(file)
      header = next(reader)
      data = list(reader)
  except FileNotFoundError :
    print(f"Error: file '{'produits.csv'}' does not exist")
    return
  except Exception as e :
    print(f"Error: {e}")
    return
  if low < high :
    pi = partition(data, low, high)
    quicksort('produits.csv', low, pi - 1)
    quicksort('produits.csv', pi + 1, high)
  sorted_table(data)
  with open('produits.csv','w', newline='') as file :
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

def partition(data, low, high) :
  pivot = float(data[high][2])
  i = low - 1
  for j in range(low, high) :
    if float(data[j][2]) <= pivot :
      i += 1
      data[i], data[j] = data[j], data[i]
  data[i + 1], data[high] = data[high], data[i + 1]
  return i + 1

def sorted_table(data) :
  print("Sorted Data by Quantity : ")
  for row in data :
    print(row)

# merge sort price
def merge_sort(data, key_index) :
  if len(data) > 1 :
    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]
    merge_sort(left_half, key_index)
    merge_sort(right_half, key_index)
    i = j = k = 0
    while i < len(left_half) and j < len(right_half) :
      if float(left_half[i][key_index]) < float(right_half[i][key_index]) :
        data[k] = left_half[i]
        i += 1
      else :
        data[k] = right_half[j]
        j += 1
      k += 1
    while i < len(left_half) :
      data[k] = left_half[i]
      i += 1
      k += 1
    while j < len(right_half) :
      data[k] = right_half[j]
      j += 1
      k += 1

merge_sort(data, 3)

# alphabetical bubble sort of product names
def sort_alphabetically(data) :
  n = len(data)
  for i in range(n) :
    for j in range(0, n - i - 1) :
      if data[j][1].lower() > data[j + 1][1].lower() :
        data[j], data[j + 1] = data[j + 1], data[j]
  for row in data :
    print(row)