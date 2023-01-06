
import random

def hello_theinfolab():

  while True:

    A = random.randint(1,9)
    B = random.randint(1,9)
    C = A * B

    if C == 4:
      print("Success!")
      print("A:", A)
      print("B:", B)
      break

    else:
      print("A:", A)
      print("C:", C)


hello_theinfolab()
