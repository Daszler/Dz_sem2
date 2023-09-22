#  Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.
from math import gcd
import fractions
 
n1, d1 = map(int, input('Введите первую дробь в формате a/b: ').split('/'))
n2, d2 = map(int, input('Введите вторую дробь в формате a/b: ').split('/'))
 
if d1 == d2:
    print(f'Сумма дробей: {n1 + n2}/{d1}')
else:
    cd = int(d1 * d2 / gcd(d1, d2))
    rn = int(cd / d1 * n1 + cd / d2 * n2)
    g1 = gcd(rn, cd)
    n = int(rn / g1)
    d = int(cd / g1)
    print(f'Сумма дробей: {n}/{d}'if n != d else n)
    print(f'Десятичная дробь: {n / d}')

product_numerator = int(n1 * n2)
product_denumerator = int(d1 * d2)
g2 = gcd(product_numerator, product_denumerator)
pr_num = int(product_numerator / g2)
pr_denum = int(product_denumerator / g2)


print(f'Произведение дробей: {pr_num}/{pr_denum}, десятичная дробь: {product_numerator/product_denumerator}')

f_one = fractions.Fraction(n1, d1)
f_two = fractions.Fraction(n2, d2)

print(f'Проверка сложения: {f_one + f_two}, десятичная: {float(f_one + f_two)}')
print(f'Проверка умножения: {f_one * f_two}, десятичная: {float(f_one * f_two)}')


# ✔ Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

num = int(input('Введите число в десятичной системе: '))
print(f'Встроенная функция hex -> {hex(num)}')


def self_hex(number: int) -> str:
    if not number:
        return '0x0'
    result = ''
    hex_letters = list('0123456789abcdef')
    while number > 0:
        result = hex_letters[number % 16] + result
        number //= 16
    return '0x' + result


print(f'Собственная функция self_hex -> {self_hex(num)}')