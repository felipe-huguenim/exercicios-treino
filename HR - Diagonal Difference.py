#Calcule a diferença ABSOLUTA entre a diagonal esquerda e direita da matriz

def diagonalDifference(matriz):
  n = len(matriz)
  leftdiag = 0
  rightdiag = 0
  for i in range(n):
    leftdiag += matriz[i][i]
    rightdiag += matriz[i][n - 1 -i]
  return abs(leftdiag - rightdiag)

print(diagonalDifference([
  [11, 2, 4],
  [4, 5, 6],
  [10, 8, -12]
  ]))