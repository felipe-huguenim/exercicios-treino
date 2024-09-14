def plusMinus(arr):
  n = len(arr)

  positive = 0
  negative = 0
  zero = 0
  for i in arr:
    if i > 0:
      positive += 1
    elif i < 0:
      negative += 1
    else:
      zero += 1
  ratiopos = positive / n
  rationeg = negative /n
  ratiozero = zero / n
  print(f'{ratiopos:.6f}')
  print(f'{rationeg:.6f}')
  print(f'{ratiozero:.6f}')

plusMinus([-4, 3, -9, 0, 4, 1])