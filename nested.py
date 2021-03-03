
car={
"Brand":"RangeRover",
"Electric":False,
"year":2019,
"color":["red","blue","white",100]
}
print(car)
#looping in dictionery
for x in car:
  print(x)
for x in car.values():
  print(x)
for x in car.keys():
  print(x)
for x,y in car.items():
  print(x,y)
#Nested dictioneries
myFamily={
"Child1":{
"Name":"Rashford",
"Year":1997
},
"Child2":{
"Name":"Fernandes",
"Year":1994
},
"Child3":{
"Name":"Pogba",
"Year":1995
},
}
print(myFamily)
  
