# Se eligio utilizar el modulo string de python en lugar de expresiones regulares para respetar las palabras con acento (en español).
import string

def rep_in_string(frase: str) -> dict:

   """
   Funcion que recibe un frase como parametro y retorna un diccionario con la cantidad de veces que se repite cada palabra en la frase. Se omiten caracteres especiales y numeros.
   args = frase: str
   """

   # Almacenamos valores de caracteres que no son letras: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.¿0123456789
   puntuacion = string.punctuation + '¿' + string.digits

   # Modificamos la frase dada eliminando caracteres especiales y numeros, y convirtiendo a minisculas
   frase = ''.join(filter(lambda x : str(x) not in puntuacion, frase.lower()))

   # Retornamos un diccionario con pares PALABRA: Cantidad de repeticiones, previamente convertimos la frase a una lista
   return {p: frase.split().count(p) for p in frase.split()}


if __name__ == '__main__':
   rep_in_string("Hola, ¿cómo están las cosas? ¿Cómo estás? ¿Eres desarrollador? Yo también soy desarrollador")
   rep_in_string("Hi how are things? How are you? Are you a developer? I am also a developer")