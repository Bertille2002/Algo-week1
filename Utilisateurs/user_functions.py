import csv
from datetime import date

# menu display options
def display_menu():
    print("\nInteractive Menu:")
    print("1. Change user data")
    print("2. Add a new user")
    print("3. Delete a user")
    print("4. Close file")
    option = input("Enter your choice (1-4): ")
    return option

# change data function
def change_data() :
    row_to_change = input("Enter your username : ")
    value_to_change = input("Enter the data you wish to change (username, password) : ")
    if value_to_change not in ['username', 'password'] :
        print("Invalid input")
        return
    replacement_value = input(f"Enter your new {value_to_change} : ")
    try : 
        with open('users.csv', 'r') as file : 
            reader = csv.reader(file)
            rows = list(reader)
            user_found = False
            for row in rows : 
                if row[3] == row_to_change : 
                    user_found = True
                    if value_to_change == 'username' :
                        row[3] = replacement_value
                    elif value_to_change == 'password' :
                        row[4] = replacement_value
                    break
            if not user_found :
                print(f"No account with username {row_to_change} was found.")
                return
        with open('users.csv', 'w', newline='') as file :
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Your {value_to_change} has been updated successfully.")
    
    except FileNotFoundError : 
        print("Error: file 'user_data.csv' not found")
    except Exception as e :
        print(f"An error occurred : {e}")

# add new product
def get_next_id() :
    with open('user_data.csv','r',newline='') as file :
        reader = csv.reader(file)
        rows = list(reader)
        last_row = rows[-1]
        last_id = int(last_row[0])
        return last_id + 1

def new_user() :
  new_name = input("Enter your first name : ")
  new_lname = input("Enter your last name : ")
  new_username = input("Enter your username : ")
  new_password = input("Enter your password : ")
  new_date = date.today()
  new_id = get_next_id()
  with open('user_data.csv','r',newline='') as file :
    reader = csv.reader(file)
    for row in reader :
        existing_username = row[3]
        if existing_username == new_username :
            raise ValueError("Error: username already exists.")
  new_row = [new_id,new_name,new_lname,new_username,new_password,new_date]
  with open('user_data.csv', 'a', newline='') as file :
    writer = csv.writer(file)
    writer.writerow(new_row)
  print("New account created successfully.")
  with open('user_data.csv', 'r', newline='') as file :
    content = file.read()
    print(content)

# delete product row
def delete_user(row_to_delete) :
  row_to_delete = input("Enter your username to delete account : ")
  try :
    with open('user_data.csv', 'r') as file : 
      reader = csv.DictReader(file)
      rows = [row for row in reader if row['username'] != row_to_delete]
    if len(rows) == 0 :
      print(f"No row with Name = '{row_to_delete}' was found.")
      return
    with open('user_data.csv', 'w', newline='') as file :
      fieldnames = ['id', 'first_name', 'last_name', 'username', 'password', 'signup_date']
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(rows)
    print(f"The product : {row_to_delete} has been deleted.")

  except FileNotFoundError:
    print(f"Error: The file '{users}' does not exist.")
  except KeyError:
    print(f"Error: The column 'P_name' does not exist in the file.")
