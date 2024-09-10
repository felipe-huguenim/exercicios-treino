#Inserir valor do produto
#Adicionar a taxa de serviço
#Mostrar o valor total com a taxa de serviço adicionada
while True:
  valor = int(input("Valor do pedido: "))
  taxa = valor * 10 / 100
  total = valor + taxa

  print("Valor do pedido: R$",valor)
  print("Taxa de serviço: R$",taxa)
  print("Total a pagar: R$", total)
