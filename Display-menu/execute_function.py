### function to execute everything ###
import csv
from functions import *

def main():
  produits = 'produits.csv'
  while True :
    input = display_menu()
    if input == "1" :
      view_names()
    elif input == "2" :
      new_product()
    elif input == "3" :
      delete_product()
    elif input == "4" :
      binary_search()
    elif input == "5" :
      data = load_data(produits)
      print("Choose sorting method:")
      print("1. Sort by Quantity (QuickSort)")
      print("2. Sort by Price (MergeSort)")
      print("3. Sort by alphabetical order")
      sort_choice = input("Choose a method: ")
      if sort_choice == "1" :
        quicksort(data, 0, len(data) - 1)
        sorted_table(data)
      elif sort_choice == "2" : 
        merge_sort(data, 3)
        print("Sorted Data by Price:")
        for row in data:
          print(row)
      elif sort_choice == "3" :
        sort_alphabetically(data)
      else : 
        print("Invalid option.")
    elif input == "6" :
      print("Closing program.")
      break
    else :
      print("Invalid input.")

if __name__ == "__main__" :
  main()