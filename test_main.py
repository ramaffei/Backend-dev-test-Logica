from ejercicios import ejercicio1 as ej1
from ejercicios import ejercicio2 as ej2
from ejercicios import ejercicio3 as ej3

import pytest

def test_ej1():
   assert ej1.fizz_buzz_2(1, 15) == [
      '01', '02', 'Fizz', '04', 'Buzz', 'Fizz', '07', '08',  'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'Fizz Buzz'
   ]


@pytest.mark.parametrize(
   "n, expected",
   [
      (5, 5),
      (10, 55),
      (15, 610),
      (20, 6765),
      (30, 832040)
   ])
def test_ej2(n, expected):
   assert ej2.ret_fibonacci_iter(n) == expected

@pytest.mark.parametrize(
   "f, expected",
   [
      ("Hola Don Pepito, hola Don Jose", {'hola': 2, 'don': 2, 'pepito': 1, 'jose': 1}),
      ("¿Paso usted ya por casa?, Por su casa yo pase.", {'paso': 1, 'usted': 1, 'ya': 1, 'por': 2, 'casa': 2, 'su': 1, 'yo': 1, 'pase': 1})
   ])
def test_ej3(f, expected):
   assert ej3.rep_in_string(f) == expected