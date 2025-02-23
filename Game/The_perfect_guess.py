import random
n = random.randint(1,100)

a = -1
guess = 0
while(a!=n):
  a = int(input("It's guess time guess a no from 1 to 100: "))
  guess+=1
  if (n>a):
      print("higher no please")
  elif(n<a):
      print("lower no please")

print(f"you guess right no {n} correct in {guess} attempt ")