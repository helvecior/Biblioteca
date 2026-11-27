def area_of_circle(raio):
    result = raio * raio
    return result

print("\nSeja bem-vindo à calculadora de áreas de formatos geométricos!\n")

raio = int(input("Qual o valor do raio do círculo que deseja calcular? "))

print(f"The area of a circle which side is {raio} is equal to {area_of_circle(raio)}")
