import f

while True:
  print("Menu")
  print("1: Cadastrar")
  print("2: Listar")
  print("0: Sair")
  op = input("Escolha Uma Opção: ")
  
  if op == "1":
    f.cadastrar()
    
  
  elif op == "2":
    f.listar()
    
  elif op == "0":
    break
  
  else:
    print("Opção invalida...")