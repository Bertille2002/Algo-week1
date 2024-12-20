### Menu interactif ###
import csv
from functions import *

# fonctions options du menu 
def main():
  produits = 'produits.csv' # definir le fichier pour appel dans fonctions 
  while True :
    input = display_menu()
    if input == "1" :
      view_names() # Voir la liste des produits, noms uniquement
    elif input == "2" :
      new_product() # Ajouter un produit a la bdd (base de donnees)
    elif input == "3" :
      delete_product() # Supprimer un produit de la bdd
    elif input == "4" :
      binary_search() # Recherche d'un produit, algorithme recherche binaire
    elif input == "5" :
      data = load_data(produits) # définir les donees dans la liste produits 
      sort_choice = sort_menu()
      if sort_choice == "1" : # Tri de la bdd par quantité avec QuickSort 
        quicksort(data) 
        sorted_table(sorted_data)
      elif sort_choice == "2" : # Tri par prix avec MergeSort
        merge_sort(data, 3)
        print("Sorted Data by Price:")
        for row in data:
          print(row)
      elif sort_choice == "3" : # Tri par produit ordre alphabetique 
        sort_alphabetically(data)
      else : # Echec de la requete si la valeur saisie ne correspond pas a une option de tri défini
        print("Invalid option.")
    elif input == "6" : # Fermer le menu interactif 
      print("Closing program.")
      break
    else : # Echec de la requete si la valeur saisie ne correspond pas a une option défini
      print("Invalid input.")

if __name__ == "__main__" :
  main()