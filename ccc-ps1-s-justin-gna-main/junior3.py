#Problem J3: Art from 2020

lines = int(input("enter the number of paint drops on the canvas: "))
coordinates = ["none"] * lines
coordinatesx = [0] * lines
coordinatesy = [0] * lines

i = 0
while i < lines:
  coordinates[i] = input("enter co-ordinatesn of paint drop number " + str(i+1) + ": ") 
  i = i+1

j = 0
while j < lines:
  coordinatesx[j] = ((int(coordinates[j][0]) * 10) + int(coordinates[j][1]))
  coordinatesy[j] = ((int(coordinates[j][3]) * 10) + int(coordinates[j][4]))
  j = j + 1
#above loop is making lists of x and y coordinates 

k = 0
highestx = 0
highesty = 0
lowestx = 100
lowesty = 100
#starting variables of the highest and lowest possible points
while k < lines:
  if coordinatesx[k] > highestx:
    highestx = coordinatesx[k]
  if coordinatesy[k] > highesty:
    highesty = coordinatesy[k]
  if coordinatesx[k] < lowestx:
    lowestx = coordinatesx[k]
  if coordinatesy[k] < lowesty:
    lowesty = coordinatesy[k]
  k = k + 1
#above loop finds compares each cooridnate to find which is the highest and lowest x or y coordinates
bottomcornerx = lowestx - 1
bottomcornery = lowesty - 1 
topcornerx = highestx + 1
topcornery = highesty + 1

print(str(bottomcornerx) + "," + str(bottomcornery))
print(str(topcornerx) + "," + str(topcornery))

'''
sample input
5
44,62
34,69
24,78
42,44
64,10

sample output
23,9
65,79
'''
