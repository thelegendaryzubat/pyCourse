import inputValidator
def Run():
  print('Введите число')
  number = checkInputRange() 
  i, j = 0, -1
  max_j, max_i = number - 1, number - 1
  min_j, min_i = 0, 1
  counter = 1
  mtrx = [[0 for j in range(number)] for i in range(number)]
  while True:
    
    while j < max_j:
        j += 1
        mtrx[i][j] = counter
        counter += 1
    max_j -= 1
    
    while i < max_i:
        i += 1
        mtrx[i][j] = counter
        counter += 1
    max_i -= 1
    
    while j > min_j:
        j -= 1
        mtrx[i][j] = counter
        counter += 1
    min_j += 1
    
    while i > min_i:
        i -= 1
        mtrx[i][j] = counter
        counter += 1
    min_i += 1
    
    if j == (number - 1) // 2 and i == number // 2:
        break 
  printSpiral(mtrx,number)

def printSpiral(mtrx,number):
  for i in range(number):
    for j in range(number):
        print(mtrx[i][j], end = '\t')
    print()

def checkInputRange():
  inputNumber = inputValidator.ValidateInput()
  while(True):
    if 4<=inputNumber and inputNumber<=1000:
      return inputNumber
      break
    else: 
      print('Число меньше 4 или больше 1000, попробуйте снова') 
      inputNumber = int(input())
      continue