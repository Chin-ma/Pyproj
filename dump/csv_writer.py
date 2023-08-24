import csv
with open('innovators.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN","Name","Contribution"])
    writer.writerow([1,"Linus Torvalds","Linux Kernel"])
    writer.writerow([2,"Tim Berners-Lee","World Wide Web"])
    writer.writerow([3,"Guido Van Rossum","Python"])
    writer.writerow([4,"Denis Ritchie","C Programming"])
    writer.writerow([5,"Steve Jobs","Apple Founder"])
    