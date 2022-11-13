#@title Game Time - go ahead and play!
import random
import numpy
inps=[]
def at():
  global pr,cr,inps
  pr=0
  c=0
  print("\nYOU ARE BATTING\n")
  while True:
    inp=input("Enter your number: ")
    while inp not in ['0','1','2','3','4','5','6','7','8','9','10']:
      inp=input("Invalid entry, enter number from 0-10: ")
    inp=int(inp)
    if c>0 and c%2==0:
      ndo=(max(set(inps), key=inps.count))
    else:
      ndo=random.randint(0,10)
    print("Computer played",ndo)
    inps.append(inp)
    if ndo==inp:
      break
    else:
      pr=pr+inp
    c+=1
  print("\nRuns you scored=",pr)
def all():
  global cr,pr,inps
  cr=0
  c=0
  print("\nYOU ARE BOWLING\n")
  while True:
    inp=input("Enter your number: ")
    while inp not in ['0','1','2','3','4','5','6','7','8','9','10']:
      inp=input("Invalid entry, enter number from 0-10: ")
    inp=int(inp)
    if len(inps)>1 and c%2!=0:
      ndo=(min(set(inps), key=inps.count))
    else:
      ndo=random.randint(0,10)
    print("Computer played",ndo)
    inps.append(inp)
    if ndo==inp:
      break
    else:
      cr=cr+ndo
    c+=1
  print("\nRuns the computer scored=",cr)
a=input("Do you want to bowl or bat first?\n")
while a not in ["bowl","bat","Bowl","Bat","BAT","BOWL"]:
  a=input('Invalid option, enter bowl or bat only:\n')
if a=="bat" or a=="Bat" or a=="BAT":
  at()
  all()
if a=="bowl" or a=="Bowl" or a=="BOWL":
  all()
  at()
if pr>cr:
  print("\nYou win!!\nYou won by",pr-cr,"runs")
elif cr>pr:
  print("\nComputer wins\nComputer won by",cr-pr,"runs")
else:
  print("The game is tied with",pr,"runs")