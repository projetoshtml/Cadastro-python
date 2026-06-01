lista = []

def cadastrar():
  nome = input("Digite o seu nome: ")
  db = {
    "Nome": nome
  }
  lista.append(db)
  print("Cadstro realizado com suceso")
  
def listar():
  print(lista)

while True:
  print("Menu")
  print("1: Cadastrar")
  print("2: Listar")
  print("0: Sair")
  op = input("Escolha Uma Opção: ")
  
  if op == "1":
    cadastrar()
    
  
  elif op == "2":
    listar()
    
  elif op == "0":
    break
  
  else:
    print("Opção invalida...")