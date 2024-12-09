### function to execute everything ###
import csv
def main():
  produits = produits.csv
  while True :
    input = display_menu
    if input == "1" :
      view_names(produits)
    elif input == "2" :
      new_product(produits)
    elif input == "3" :
      delete_product(produits)
    elif input == "4" :
      binary_search(produits)
    elif input == "5" :
      print("Closing program.")
      break
    else :
      print("Invalid input.")

if __name__ == "__main__" :
  main()