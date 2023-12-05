import csv, os

path = os.path.abspath(os.path.dirname(__file__))

fields = ["name", "number", "building", "road", "block", "city", "apartment"]


def write(name, number, building, road, block, city, apartment):
    mydict = [{'name': name,'number':number,'building':building, 'road':road,'block':block,'city':city,'apartment':apartment}]

    with open(path + "/AddList.csv", 'a') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames = fields)         

        writer.writeheader() 

        writer.writerows(mydict)

print("Please Choose An Option:\n")
print("1. Write an address")

op = input("Option: ")

if op == "1":
    print("\nWriting to file")
    name = input("Name: ")
    number = input("Number: ")
    building = input("Building: ")
    road = input("Road: ")
    block = input("Block: ")
    city = input("City: ")
    apartment = input("Apartment: ")
    write(name, number, building, road, block, city, apartment)