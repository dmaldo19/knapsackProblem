#Diego Alberto Maldonado Melendez

capacidad = 80
elementos1 = {"cama" : [2200, 30], "plato" : [20, 0.5], "silla" : [300, 2.5],
            "cafetera" : [600, 4], "tv" : [2000, 18], "mesa" : [1000, 8], "taza" : [50, 0.5],
            "lampara" : [200, 2], "freidora" : [500, 1], "refri":[3000, 45]}
elementos2 = {"cama" : [2200, 30], "plato" : [20, 0.5], "silla" : [300, 2.5],
            "cafetera" : [600, 4], "tv" : [2000, 18], "mesa" : [1000, 8], "taza" : [50, 0.5],
            "lampara" : [200, 2], "freidora" : [500, 1], "refri":[3000, 45],
            "compu": [10000, 1.5], "telefono": [8000, 0.5], "bloqueador" : [200, 0.5],
            "navaja" : [600, 0.5], "libro":[100, 3]}

def encontrar_mejor_combinacion(elementos, capacidad):
    mejores_combinaciones = []
    mejor_valor = 0
    mejor_peso = 0
    elementos_lista = list(elementos.keys())
    n = len(elementos_lista)
    contadorIteraciones = 0

    for i in range(2 ** n): #Este primer for es para realizar todas las posibles combinaciones del problema (2^n)
                            #Todas las posibles combinaciones que se pueden hacer con el conjunto que se tiene
        combinacion_actual = []

        #Calcular el valor y peso de la combinacion actual
        valor_actual = 0
        peso_actual = 0

        #for para iterar los elementos de mi diccionario
        for j in range(n):
            contadorIteraciones += 1
            #Mascara de bits para saber si se debe agregar el elementos
            if (i >> j) & 1:
                elemento = elementos_lista[j]
                valor, peso = elementos[elemento]
                if peso_actual + peso <= capacidad:
                    peso_actual += peso
                    valor_actual += valor
                    combinacion_actual.append(elemento)

        if valor_actual > mejor_valor:
            mejores_combinaciones = [combinacion_actual]
            mejor_valor = valor_actual
            mejor_peso = peso_actual

    print("Iteraciones realizadas: ", contadorIteraciones)
    return mejores_combinaciones, mejor_valor, mejor_peso

#Con la lista inicial
mejores_combinaciones, mejor_valor, mejor_peso = encontrar_mejor_combinacion(elementos1, capacidad)

print("Con lista inicial: ")
print("Mejor combinacion:")
for combinacion in mejores_combinaciones:
    print(combinacion)
print("Mejor valor: $", mejor_valor)
print("Peso de los elementos: ", mejor_peso)

print("\nCon lista de prueba: ")
mejores_combinaciones, mejor_valor, mejor_peso = encontrar_mejor_combinacion(elementos2, capacidad)

print("Mejor combinacion:")
for combinacion in mejores_combinaciones:
    print(combinacion)
print("Mejor valor: $", mejor_valor)
print("Peso de los elementos: ", mejor_peso)
