
#region	GEOMETRIC FIGURES AREA CALCULATION FUNCTIONS

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

#region	FUNCTIONS FOR REDIRECTING IF CHOICES 

def circle_choice():
  raio = int(input("Qual o valor do raio do círculo que deseja calcular a área? "))
  
  print(f"The area of a circle which side is {raio} is equal to {area_of_circle(raio)}")
  
def square_choice():
  side = int(input("Qual o valor do lado do quadrado que deseja calcular a área? "))
  
  print(f"The area of the square with side length={side} is equal to {area_of_square(side)}")
  
def triangle_choice():
  base = int(input("Qual o valor da base do triângulo que deseja calcular a área? "))
  height = int(input("Qual o valor da altura do triângulo que deseja calcular a área? "))

  print(f"The area of a the triangle with base length={base} and heigth={height} is equal to {area_of_triangle(base,height)}")

def rectangle_choice():
  base = int(input("Qual o valor da base do retângulo que deseja calcular a área? "))
  height = int(input("Qual o valor da altura do retângulo que deseja calcular a área? "))
  
  print(f"The area of the rectangle with base={base} and height={height} is equal to {area_of_rectangle(base,height)}")


#endregion #! end

#region	FUNCTIONS FOR MENU 

def menu_selection():

  print("\nSeja bem-vindo à calculadora de áreas de formatos geométricos!\n")

  options = ["1. Círculo", "2. Quadrado", "3. Triângulo", "4. Retângulo"]

  choice = int(input(
      "Escolha o formato geométrico que deseja calcular a área:\n"
      + "\n".join(options)
      + "\n\nDigite o número correspondente à sua escolha: "
      ))

  #* conditional statements to redirect the user to the correct function based on their choice 

  if choice == 1: 
    circle_choice()

  elif choice == 2: 
    square_choice()

  elif choice == 3: 
    triangle_choice()

  elif choice == 4: 
    rectangle_choice()

#endregion #! end


def main():
  menu_selection()

main()
