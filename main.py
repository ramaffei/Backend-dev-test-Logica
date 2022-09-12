from ejercicios import ejercicio1 as ej1
from ejercicios import ejercicio2 as ej2
from ejercicios import ejercicio3 as ej3

if __name__ == "__main__":
   print("Ejercicio 1: Mostrar en pantalla los numeros del 1 al 100, reemplazando los multiplos de 3 por Fizz, los multiplos de 5 por Buzz, y los multiplos de ambos por Fizz Buzz\n")
   print(ej1.fizz_buzz_2(1, 100),"\n")
   print("Ejercicio 2: Resolver cualquier numero en la seria de Fibonacci\nNumero de prueba: 15\n")
   print(ej2.ret_fibonacci_iter(15),"\n")
   print("Ejercicio 3: Mostrar en pantalla la cantidad de repeticiones que tiene cada palabra de una cadena\n")
   cadena = "Hi how are things? How are you? Are you a developer? I am also a developer"
   print(f"Cadena: {cadena}\n")
   print(ej3.rep_in_string(cadena), "\n")
   print("Ejecucion finalizada")
