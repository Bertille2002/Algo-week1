### create text file ###
import csv 
with open('text.txt', 'w') as file :
    file.write('New file created !! \n')

with open('text.txt','a') as file :
    file.write('this is a test \n')
    file.close()

with open('text.txt', 'r') as file :
    content = file.read()
    print(content)