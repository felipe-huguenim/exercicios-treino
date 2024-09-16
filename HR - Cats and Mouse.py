def catAndMouse(x,y,z):
  distanceA = abs(z - x)
  distanceB = abs(z - y)
  if distanceA < distanceB:
    return 'Cat A'
  elif distanceA > distanceB:
    return 'Cat B'
  else:
    return 'Mouse C'
  
print(catAndMouse(1,2,3))
print(catAndMouse(1,3,2))