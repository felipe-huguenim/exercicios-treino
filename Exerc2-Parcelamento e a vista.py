#inserir produto
#Valor a vista (10% desconto)
#Parcelado em 3x
while True:

  try:
    produto = int(input("\nInsira o valor do produto: "))
    desconto = produto * 10 / 100
    break

  except ValueError:
    print("\nEntrada inválida. Por favor, insira um número.")


while True:
  print("\nForma de pagamento: \n - (1) À vista \n - (2) Parcelado")
  formapagamento = input()
  if formapagamento == "1":
    valor_a_pagar = produto - desconto
    print(f"\nR$,{valor_a_pagar:.2f}")
    break


  elif formapagamento == "2":
    while True:
      print("\nEscolha o número de parcelas \n (2) Duas vezes \n (3) Três vezes")
      quantidadeparcelas = input()
      if quantidadeparcelas == "2":
        valor_a_pagar = produto / 2
        print(f"\nA pagar: R${valor_a_pagar:.2f} 2x sem juros")
        break


      elif quantidadeparcelas == "3":
        valor_a_pagar = produto / 3
        print(f"\nA Pagar: R${valor_a_pagar:.2f} 3x sem juros")
        break
      else:
        print("\nQuantidade inválida de parcelas")
    break
  else:
    print("\nOpção inválida")