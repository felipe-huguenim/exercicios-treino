# ar = [1,2,3] 
# Somar os itens do array
# Subtrair os itens do array
# Multiplicar os itens do array
# Fazer a média aritimética do array

def simpleArraySum(ar):
  sum_all = 0
  for i in (ar):
    sum_all += i
  return sum_all

def simpleArraySub(ar):
  sub_all = 0
  for i in (ar):
    sub_all -= i
  return sub_all

def simpleArrayMult(ar):
  mult_all = 0
  for i in (ar):
    mult_all *= i
  return mult_all

def mediaAritmetica(ar):
  sum_all = 0
  for i in (ar):
    sum_all += i
    mediaArit = sum_all / len(ar)
  return mediaArit

# -> 0 Pois os valores base foram definidos como 0 (sum_all,sub_all,mult_all = 0)
print(simpleArraySum([1,2,3])) # R: 6 (0+1+2+3) 
print(simpleArraySub([1,2,3])) # R: -6 (0-1-2-3)
print(simpleArrayMult([1,2,3]))# R: 0 (0*1*2*3)
print(mediaAritmetica([1,2,3]))# R: 2 ((0+1+2+3) / 3)