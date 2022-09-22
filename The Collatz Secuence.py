"""
User: Juan Manuel Hernández Solano 

A Collatz Secuence function
The user input a number and the function return its collatz secuence

 """

def collatz(num):
  try:
    num = int(input("Enter number: "))
    print(num)
    while num != 1:
      if num % 2 == 0:
        num = num // 2
        print(num)
      else:
        num = (num * 3) + 1 
        print(num)
  except ValueError:
    print("Enter a integer number ")
  return 
collatz(num)
