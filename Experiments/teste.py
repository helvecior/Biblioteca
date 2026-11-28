
#region	FUNCTIONS FOR MENU 

def shape_selection_menu():

  print("\nSeja bem-vindo à calculadora de áreas de formatos geométricos!\n")

  options = ["1. Círculo", "2. Quadrado", "3. Triângulo", "4. Retângulo"]

  choice = int(input(
      "Escolha o formato geométrico que deseja calcular a área:\n"
      + "\n".join(options)
      + "\n\nDigite o número correspondente à sua escolha: "
      ))

  #* conditional statements to redirect the user to the correct function based on their choice 

  if choice == 1: 
    shape = "círculo"
    measure_simple = "raio"
    simple_format_answer(measure_simple, shape)

  elif choice == 2: 
    shape = "quadrado"
    measure_simple = "lado"
    simple_format_answer(measure_simple, shape)

  elif choice == 3: 
    shape = "triângulo"
    measure_name_1 = "base"
    measure_name_2 = "altura"
    complex_format_answer(measure_name_1, measure_name_2, shape)

  elif choice == 4:
    shape = "retângulo"
    measure_name_1 = "base"
    measure_name_2 = "altura"
    complex_format_answer(measure_name_1, measure_name_2, shape)

#endregion #! end

#region	FUNCTIONS THA CALCULATE AND PRESENT THE AREA OF SELECTED GEOMETRIC SHAPES

def simple_format_answer(measure_simple, shape):
  
  # perguntar ao usuário o valor do raio ou do lado, dependendo da forma geométrica selecionada
  values_colected = int(input(f"Qual o valor do {measure_simple} do {shape} que você deseja calcular a área? "))
  
  if shape == "círculo":
    area = values_colected ** 2 * 3.14
    print(f"A área do {shape} é: {area:.2f}")

  if shape == "quadrado":
    area = values_colected ** 2
    print(f"A área do {shape} é: {area:.2f}")

def complex_format_answer(measure_name_1, measure_name_2, shape):
  
  print(f"Qual o valor do {first_value} e da {second_value} do {shape} que você deseja calcular a área? ")
  
  first_value = int(input(f"{measure_name_1}: "))
  second_value = int(input(f"{measure_name_2}: "))

  values_colected = [ first_value, second_value ]

  if shape == "triangle":
    print(f"O resultado da área do {shape} é: {(values_colected[0] * values_colected[1]) / 2 }.")

  if shape == "rectangle":
    print(f"O resultado da área do {shape} é: {values_colected[0] * values_colected[1]}.")

#endregion



def main():
  shape_selection_menu()

main()
