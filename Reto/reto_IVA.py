

#############################################################################################################################################
# PROGRAMA CALCULO IVA:


print("\n")
print("-----------------------------")
print("    PROGRAMA CALCULO IVA     ")
print("-----------------------------")
print("\n")
  
dato = float(input("Introduce importe: € "))                                       # se solicita un 'importe' al usuario a través de un 'input(float)'
calculo_iva = float(input("Introduce IVA: % "))                                    # se solicita un valor de 'IVA' a través de un 'input(float)'                 

iva = dato*(calculo_iva/100)                                                       # se calcula el IVA correspondiente a los valores recogidos anteriormente
total = dato + iva                                                                 # se realiza la 'suma' resultado del importe inicial mas el IVA calculado para posteriormente imprimir...

print("-----------------------------")      
print(f"Calculo IVA: {iva:.2f} €")                                                 # Se muestra el IVA calculado
print(f"Importe + IVA: {total:.2f} €")                                             # Se muestra el resulado de la suma (importe + IVA)





############################################################################################################################################
# PRUEBAS AUTOMATIZADAS:


historicos = ["Ana",200,"Pedro",340,"Angel",480]                                   # se declaran unos historicos en una 'lista' con varios 'items' de tipo 'int' y 'str'
iva_fijo = 21                                                                      # se declara un valor de IVA fijo: 21% (variable 'int')

print("\n")
print("-----------------------------")
print("------- P R U E B A S -------")
print("-----------------------------")
print("\n")
print("IMPORTES fijados:")
print("-----------------------------")
print("Ana = 200")
print("Pedro = 340")
print("Angel = 480")
print("-----------------------------")
print("\n")
print("IVA fijado:")
print("-----------------------------")
print("21%")
print("-----------------------------")
print("\n")
print("RESULTADOS:")
print("-----------------------------")


for i in historicos:                                                               # se recorren los diferentes 'items' de la lista 'Historicos' con un bucle 'FOR'
    if isinstance (i, int):                                                        # se comprueba que los 'items' sean de tipo 'int'
        print(f"Importe ({i}) + IVA (21%) = {(i + (i * iva_fijo/100)):.2F}")       # se imprime el resultado de la operacion (importe + IVA) para los 'items(int)' encontrados por el bucle
        print("-----------------------------")
    else:                                                                          # si el 'item' de la lista NO es un 'int'...
        print(i)                                                                   # se imprime el 'item'

print("\n")

                    








