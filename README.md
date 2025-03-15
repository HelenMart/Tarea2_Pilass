## Caracteristicas
- Funcion capaz de evaluar una expresion matematica, comprobando si los parentesis o signos de agrupacion estan nivelados

Ejemplo: 

Expresion 1: [(8-9)+(4/8)]  ----> Expresion nivelada

Expresion 2: [(8-9)+((4/8)] ----> Expresion desnivelada

- Funcion de conversion de una expresion matematica infija a una expresion posfija

Ejemplo:

Expresion 1: (8 -9  )+12     ---> Resultado: 8 9 12 - +

Expresion 2: [(5-6)+(14/2)] ---> Resultado: 5 6 14 2 - + /

## Conceptos utiizados
- Pilas
- Listas
- Bucles
- Signos

## Clases / Funciones principales 
### 1. Balanza 
`````python
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
`````

### 2. Conversion de notacion infija a posfija
```python
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
```
