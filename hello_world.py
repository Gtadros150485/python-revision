import csv
from pathlib import Path
import matplotlib.pyplot as plt
box1 = 12 #Number
box2 = "Steven" #String
box3 = 3.1442342
box4 = ["My First Name", "My Second Name"]
list_of_numbers = [33,453,4353,5345,3]


first_name = "George"
second_name = "Michael"
full_name = f" Hello  my name is {first_name} {second_name}"

string1 = "python  "
string2 = "python   "
string3 = "python    "

nostarch_url = 'https://httpsnos.comtarch.com'

#Arth Operations

long_number = 10_000_000_000

PI_VALUE = 3.14
print(PI_VALUE)
PI_VALUE = 3.15
print(PI_VALUE)

list1 = [3, 3,3,3,10]
print(list1)
list1[0] = 5
print(list1)
list1.append(9)
print(list1)
list1.insert(0,7)
print(list1)
list1.pop()
print(list1)
list1.pop()
print(list1)
list1.pop(0)
print(list1)
list1.remove(3)
print(list1)

print(sorted(list1))
print(len(list1))

#define a tuple
tupl = (3,9)
print(tupl)

#creating a function that add two variables
def add_two(v1, v2):
    return v1+v2
def print_two_addition(v1,v2):
    print(v1+v2)
print(add_two(3,6))
print_two_addition(3,7)

path = Path("/Users/a12345/PycharmProjects/python-crach-course/email.csv")

lines =  path.read_text().splitlines()

for line in lines:
    for word in line.split(";"):
        print(word)
    print(line)

#enumerate return a function and the index and the data
for index,header_line in enumerate(lines):
    print(index, header_line)
number_data = []
for line in lines:
    number_data.append(line.split(";")[1])
number_data.pop(0)
print(number_data)

fig, ax = plt.subplots()

ax.plot(number_data)
plt.show()
