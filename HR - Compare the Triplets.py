# Compare os arrays
# Atribua pontos de acordo com o maior
# retorne os pontos 

def compareTriplets(a, b):
    A_points = 0
    B_points = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            A_points += 1
        elif b[i] > a[i]:
            B_points += 1
    return (A_points, B_points)

result = compareTriplets([5,6,7],[3,6,10])
print(result)