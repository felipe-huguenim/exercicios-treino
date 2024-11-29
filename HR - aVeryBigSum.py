def aVeryBigSum(ar):
  bigsum = 0
  for i in ar:
    bigsum += i
  return bigsum

ar1 = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

print(aVeryBigSum(ar1))