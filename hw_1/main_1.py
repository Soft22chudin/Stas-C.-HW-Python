"""
Найдите сумму цифр трехзначного числа.
"""
import math
sum = int(input())
a = math.floor(sum * 0.01)
b = math.floor((sum - a * 100) * 0.1)
c = sum - a * 100 - b * 10
print(str(a) + " " + str(b) + " " + str(c))
print(a+b+c)