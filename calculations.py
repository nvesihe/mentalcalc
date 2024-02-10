import random




def addition():
  state = True
  while state:
    x = random.randint(0,101)
    y = random.randint(0,101)
    num = x+y
    print('{0} + {1}'.format(x,y))
    answer = int(input('(0 quits) Answer: '))
    if answer == num:
      print("Correct!")
    elif answer == 0:
      break
    else:
      print("Wrong! Answer is " + str(num))

def check():
  t = True
  while t: 
    y = random.randint(0,101)
    x = random.randint(0,101)
    if x < y:
      continue
    else:
      substraction(x,y)
      
      
def substraction(x,y):
    num = x-y
    print('{0} - {1}'.format(x,y))
    answer = int(input('(0 quits) Answer: '))
    if answer == num:
      print("Correct!")
      check()
    elif answer == 0:
      exit()
    else:
      print("Wrong! Answer is " + str(num))
      check()










i = True
while i == True:
  option = input("Choose: addition is a and substraction is s (ext to exit the program): ")
  if option == "a":
    addition()
  elif option == "s":
    check()
  elif option == "ext":
    break
  else:
    print("incorrect option. please try again.")

  





