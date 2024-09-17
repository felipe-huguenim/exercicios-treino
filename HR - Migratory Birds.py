def migratoryBirds(arr):
  l = [0] * len(arr)
  for i in arr:
    l[i] += 1
  print(l)
  return l.index(max(l))


print(migratoryBirds([1, 4, 4, 4, 5, 3]))