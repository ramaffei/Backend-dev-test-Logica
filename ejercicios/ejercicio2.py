# Fibonacci utilizando recursividad, sobrecarga la memoria para numeros grandes.
def ret_fibonacci_rec(num: int) -> int:
   """
   Funcion que recibe un numero (n) y aplica la seria de Fibonacci para retornar el valor correspondiente.
   args = num: int
   """
   if num == 0 or num == 1:
      return num
   
   return ret_fibonacci_rec(num-1)+ret_fibonacci_rec(num-2)

# Alternativa utilizando iteracion, mejora considerablemente los tiempos de respuesta.
def ret_fibonacci_iter(num: int) -> int:
   
   """
   Funcion que recibe un numero (n) y aplica la seria de Fibonacci de manera recursiva para retornar el valor correspondiente.
   args = num: int
   """
   
   a, b = 0, 1

   for n in range(num):
      c = a+b
      a = b
      b = c

   return a
if __name__ == "__main__":
   print(ret_fibonacci_iter(7))
   print(ret_fibonacci_iter(100))