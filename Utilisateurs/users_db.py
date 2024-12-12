import csv

user_data = [
    [1,"Alice","Beaumont","alice12","9REqJgX8cLHr0ly","12-05-24"],
    [2,"Jean","Dubois","JD_3","GCf3Xky7GC67FTA","27-12-23"],
    [3,"Simon","Schmitt","Simsum","Sb2hqJ9Cm9wzQoB","18-10-21"],
    [4,"Chloe", "Lukasiak", "chlobird","sKOl3DF3rBZDJQl","01-08-15"],
    [5,"Maddie", "Ziegler", "madz","nx77353Wgc5","15-02-14"],
    [6,"Aaron", "Colin", "aaroncol","f3qSSljLHuv","30-11-22"]
]

with open('users.csv', 'w', newline='') as file :
    writer = csv.writer(file)
    field = ["ID","first_name", "last_name", "username","password","signup_date"]
    writer.writerow(field)
    writer.writerows(user_data)
