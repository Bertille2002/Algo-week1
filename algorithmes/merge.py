import csv

data = [
    [1,"pomme","5","18.2","12-05-24"],
    [2,"oeuf","9","43.1","27-12-24"],
    [3,"pasta","27","1.05","18-10-27"],
    [4, "riz", "15", "2.3", "01-08-25"],
    [5, "lait", "8", "0.99", "15-02-24"],
    [6, "fromage", "20", "5.5", "30-11-24"]
]

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

merge_sort(data, 3) # sort by price (column index 3)

print("Data sorted by price : ")
for row in data :
  print(row)