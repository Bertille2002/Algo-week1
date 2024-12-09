import csv

data = [
    [1,"pomme","5","18.2","12-05-24"],
    [2,"oeuf","9","43.1","27-12-24"],
    [3,"pasta","27","1.05","18-10-27"],
    [4, "riz", "15", "2.3", "01-08-25"],
    [5, "lait", "8", "0.99", "15-02-24"],
    [6, "fromage", "20", "5.5", "30-11-24"]
]

def tri_rapide(data, low, high) :
  if low < high :
    pi = partition(data, low, high)
    quicksort(data, low, pi - 1)
    quicksort(data, pi + 1, high)

def partition(data, low, high) :
  pivot = float(data[high][3])
  i = low - 1
  for j in range(low, high) :
    if float(data[j][3]) <= pivot :
      i += 1
      data[i], data[j] = data[j], data[i]
  data[i + 1], data[high] = data[high], data[i + 1]
  return i + 1

def sorted_table(data) :
  print("Sorted Data by Price : ")
  for row in data :
    print(row)

quicksort(data, 0, len(data) - 1)
sorted_table(data)