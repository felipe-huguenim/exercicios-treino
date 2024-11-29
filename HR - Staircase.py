def staircase(n):
  for i in range(n):
    pyramid = '#'
    spaces = ' '

    width = (n - i) - 1
    blocks = i + 1
    print (spaces * width + pyramid * blocks)
  
  
print(staircase(90))