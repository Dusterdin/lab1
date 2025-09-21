# prob.py
# -*- coding: utf-8 -*-
import sys

print("="*40)
print("Python version:", sys.version)
print("="*40)

# 1. print - як функція
print("Hello from print function") # працює у Python 3.7 а у Python 2.7 : print"Hello from print statement"


# 2. Ділення цілих чисел
print("5/2 =", 5/2)            # у Python 2 => 2, у Python 3 => 2.5
print("5//2 =", 5//2)          # обидва дають 2

# 3. Типи рядків
s = "Привіт"
print("Type of 's':", type(s))  # Python 2 => str (bytes), Python 3 => str (unicode)

# 4. input vs raw_input
try:
    val = input("Enter a number3: ")  # у Python 2 це виконує eval()
except NameError:
    val = raw_input("Enter a number2: ")  # існує тільки в Python 2
print("You entered:", val)

# 5. xrange vs range
try:
    r = xrange(3)  # тільки Python 2
except NameError:
    r = range(3)   # Python 3
print("Range object:", r)

# 6. Розподіл типів int/long
big_num = 10**40
print("Big number type:", type(big_num))  # Python 2 => long, Python 3 => int

# 7. next() для ітераторів
it = iter([1,2,3])
print("Next element:", next(it))  # Python 3 функція next()
# У Python 2 працює також it.next() до цього

# 8. Методи словників
d = {"a":1, "b":2}
print("Keys:", list(d.keys()))  # Python 2 => список, Python 3 => view object

# 9. Порівняння різних типів
try:
    print("Compare int and str:", 1 < "2")  # Python 2 дозволяє, Python 3 -> помилка
except Exception as e:
    print("Error:", e)

# 10. print unicode
try:
    print(u"Привіт, Unicode!")  # Python 2 потребує 'u' префікс, Python 3 - ні
except Exception as e:
    print("Unicode error:", e)
