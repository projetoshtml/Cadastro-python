import funcoes as fc

while True:
  print("Menu")
  print("1: Cadastrar")
  print("2: Listar")
  print("0: Sair")
  op = input("Escolha Uma Opção: ")
  
  if op == "1":
    fc.cadastrar()
    
  
  elif op == "2":
    fc.listar()
    
  elif op == "0":
    break
  
  else:
    print("Opção invalida...")