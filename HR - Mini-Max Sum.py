#Ache a menor e a maior soma possível dado os números contidos no Array

def miniMaxSum(arr):
  max_sum = 0
  min_sum = 0
  arraySum = 0
  for i in arr:
    arraySum += i
  max_sum = arraySum - min(arr)
  min_sum = arraySum - max(arr)
  print(min_sum, max_sum)

miniMaxSum([1,2,3,4,5])