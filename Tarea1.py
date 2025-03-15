def balanza(expresion):
  entrada = []
  salida = []
  
  for caracter in expresion:
    if caracter in '{([':
      entrada.append(caracter)
    elif caracter in '})]':
      salida.append(caracter)

  tamaño1 = len(entrada)
  tamaño2 = len(salida)

  if(tamaño1 == tamaño2):
        print(f"La expresion esta nivelada con: ", tamaño1, "expresiones de entrada y ",tamaño2,"expresiones de salida")
  elif(tamaño1<tamaño2 | tamaño1>tamaño2):
        print(f"La expresion no esta nivelada")

def conversion(Lista):
   operadores = []
   salida = " "

   for recorrer in Lista:
      if recorrer in '12345678910':
         salida += recorrer
      elif recorrer in '-+*/' :
         operadores.append(recorrer)
   while operadores:
      salida += operadores.pop(0)
  
   return salida

Expresion = "(1+2)/[(9+9)-8])"
print(balanza(Expresion))

expresion = "1 + 8 * 9 - 10 ( 5 * 8 )"
print(conversion(expresion))
