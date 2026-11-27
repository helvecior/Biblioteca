
def colect_username(nome):
  nome = input("Olá usuário! Qual o seu nome ? ")
  return nome

def colect_age_data(ano_nascimento,ano_atual):
  ano_nascimento = (int(input(f"Qual o ano em que você nasceu {colect_username()}? ")))
  ano_atual = (int(input(f"Qual o ano em que você está {colect_username()} ? ")))
  return ano_nascimento, ano_atual

def calcular_idade(ano_nascimento,ano_atual):
  return ano_atual - ano_nascimento 

def present_age():
  print(f"Você nasceu em {ano_nascimento} e você tem aproximadamente {calcular_idade(colect_age_data(ano_nascimento,ano_atual))} anos de idade.")

def menu():
  print(f"Como você está, {nome}?\nO que você deseja fazer ?")
  print(f"As opções são:\n1.Calcular minha idade\n2.Saber que dia é hoje\n3.Fazer um teste de matemática:)")
  resposta = input(f"\n{nome}, digite a opção que você quer escolher.")
  
  if (resposta == 1):
    colect_age_data()
    present_age()

  elif (resposta == 2):
    print(datetime.date())
    
  elif (resposta == 3): 
    print ("teste de matemática")

def main(): 
  colect_username()
  menu()