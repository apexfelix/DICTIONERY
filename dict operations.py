#Dictionery
car={
"Brand":"RangeRover",
"Electric":False,
"year":2019,
"color":["red","blue","white",100]
}
print(car)
#Accesing items in dictionery
x=car["Brand"]
print(x)
#Getting Keys and values
y=car.keys()
print(y)
z=car.values()
print(z)
#Cheking if key exists
if "model" in car:
  print("yes")
else:
  print("no")
if "color" in car:
  print("yes")
#Changing Items
car["Brand"]="Toyota"
print(car)
#addind items
car["Competitors"]=["Rangerover","Subaru","lamboghini"]
print(car)
#removing items
#pop()
#popitem()
#del
#clear()
car.pop("year")
print(car)
del car["color"]