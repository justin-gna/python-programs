# Problem J4/S1: Flipper from 2019
numberpositions = [1,2,3,4]
print(numberpositions[0], numberpositions[1])
print(numberpositions[2], numberpositions[3])

txt = input("enter h/v to flip: ")
txt = txt.lower()
discontinue = False
i = 0
while i < len(txt):
   #abcd are here to avoid the probelm of new values overwritin old values
  A = numberpositions[0]
  B = numberpositions[1]
  C = numberpositions[2]
  D = numberpositions[3]
  if txt[i] == "h":
    numberpositions[0] = C
    numberpositions[1] = D
    numberpositions[2] = A
    numberpositions[3] = B 
  elif txt[i] == "v":
    numberpositions[0] = B
    numberpositions[1] = A
    numberpositions[2] = D
    numberpositions[3] = C
  else:
    discontinue = True
    break
  i = i + 1
if discontinue == True:
  print("please only enter h/v, close the program and try again")
else:
  print(numberpositions[0], numberpositions[1])
  print(numberpositions[2], numberpositions[3])