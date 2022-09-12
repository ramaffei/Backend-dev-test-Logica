def fizz_buzz() -> None:
   
   """ Funcion que que itera numeros 1 al 100 y muestra en pantalla "Fizz" si el numero es multiplo de 3, "Buzz" si el numero es multiplo de 5 ó "Fizz Buzz" si el numero es multiplo de 3 y 5. Si no se cumple alguna de estas condiciones, muestra el numero."""

   for m in range(1, 101):
      salida = m
      if m % 3 == 0:
         salida = "Fizz"
         if m % 5 == 0:
            salida += " Buzz"
      elif m % 5 == 0:
         salida = "Buzz"
      
      print(salida)

# Alternativa, no representa cambios en cuanto a tiempo de respuesta.
def fizz_buzz_2(desde: int = 1, hasta: int = 100) -> list:
   
   """ Funcion que recibe dos argumentos numericos y retorna una lista donde reemplaza los numeros multiplo de 3 por la cadena "Fizz", los multiplo de 5 por la cadena "Buzz" y los multiplos de 3 y 5 por la cadena "Fizz Buzz"
   args: desde (1)
         hasta (100)
   """

   result = []
   for n in range(desde, hasta+1):
      salida = ''
      salida = 'Fizz ' if n % 3 == 0 else salida
      salida += 'Buzz' if n % 5 == 0 else ''
      salida = str(n).zfill(2) if salida == '' else salida
      result.append(salida.strip()) 

   return result
if __name__ == "__main__":
   fizz_buzz()
   fizz_buzz_2(100)
            