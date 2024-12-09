import csv
def display_menu():
    print("\nInteractive Menu:")
    print("1. View products only")
    print("2. Add a new product")
    print("3. Delete a product")
    print("4. Search for a specific product")
    print("5. Close file")
    input = input("Enter your choice (1-4): ")
    return input