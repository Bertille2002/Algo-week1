import csv
from user_functions import *

def main():
  users = 'users.csv'
  while True :
    input = display_menu(users)
    if input == "1" :
      change_data(users)
    elif input == "2" :
      new_user(users)
    elif input == "3" :
      delete_user(users)
    elif input == "4" :
      print("Closing program.")
      break
    else :
      print("Invalid input.")

if __name__ == "__main__" :
  main()