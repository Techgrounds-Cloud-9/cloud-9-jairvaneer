import csv
myfile=open('exercise_8.csv', 'r+')
print(myfile.read())
about = {
"First name": input("First name: "),
"Last name": input("Last name: "),
"Job title": input("Job title: "),
"Company": input("Company: ")
}

writer = csv.writer(myfile)
writer.writerow(about.keys())
writer.writerow(about.values())
myfile.close
myfile=open('exercise_8.csv', 'r')
print(myfile.read())