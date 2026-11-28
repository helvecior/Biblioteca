
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
    measure_1 = "base"
    measure_2 = "altura"
    complex_format_answer(measure_1, measure_2, shape)

  elif choice == 4:
    shape = "retângulo"
    measure_1 = "base"
    measure_2 = "altura"
    complex_format_answer(measure_1, measure_2, shape)

#endregion #! end

#region	FUNCTIONS FOR CALCULATING AREAS OF GEOMETRIC SHAPES

def area_of_circle(raio):
    pi = 3.14159
    result = pi * raio * raio
    return result

def area_of_square(side):
    result = side * side
    return result

def area_of_triangle(base, height):
    result = (base * height) / 2 
    return result

def area_of_rectangle(base, height):
    result = base * height
    return result

#endregion #! end

#region	FUNCTIONS THA CALCULATE AND PRESENT THE AREA OF SELECTED GEOMETRIC SHAPES

def simple_format_answer(measure_simple, shape):
  values_colected = int(input(f"Qual o valor do {measure_simple} do {shape} que você deseja calcular a área? "))
  return values_colected

def complex_format_answer(measure_1, measure_2, shape):
  values_colected = int(input(f"Qual o valor do {measure_1} e da {measure_2} do {shape} que você deseja calcular a área? "))
  return values_colected
#endregion #! end



def main():
  shape_selection_menu()

main()
