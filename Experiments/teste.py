
#region	GEOMETRIC FIGURES AREA CALCULATION FUNCTIONS

def area_of_circle(raio):
    result = raio * raio
    return result

def area_of_square(side):
    result = side * side
    return result

def area_of_triangle(base, height):
    result = (base * height) / 2
    return result


#endregion #! end

#region	FUNCTIONS FOR MENU 

def menu_selection():
      options = ["1. Circle", "2. Quadrado", "3. Triângulo"]
      
      print("\nSeja bem-vindo à calculadora de áreas de formatos geométricos!\n")
      
      choice = int(input("Escolha o formato geométrico que deseja calcular a área: "))
      print("\n".join(options))
      
      if choice = 1; then 


      return choice

#endregion #! end


raio = int(input("Qual o valor do raio do círculo que deseja calcular? "))

print(f"The area of a circle which side is {raio} is equal to {area_of_circle(raio)}")

def main():
  menu_selection()
