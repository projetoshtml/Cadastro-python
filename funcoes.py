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