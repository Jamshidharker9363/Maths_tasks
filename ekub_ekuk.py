from math import gcd
from functools import reduce

def gcd_multiple(numbers):
    return reduce(gcd, numbers)

def lcm(a, b):
    return (a*b)//gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lcm, numbers)

numbers = list(map(int, input("Sonlarni bo'sh joy bilan ajratib yozing : ").split()))

ekub = gcd_multiple(numbers)
ekuk = lcm_multiple(numbers)

print(f"Kiritilgan sonlarning EKUBi -> {ekub}\nKiritilgan sonlarning EKUKi -> {ekuk}")