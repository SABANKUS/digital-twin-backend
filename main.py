# main.py
from functions import selamla, topla, carp

isim = input("İsmini gir: ")
print(selamla(isim))

x = float(input("Bir sayı gir: "))
y = float(input("Başka bir sayı gir: "))
print("Toplam:", topla(x, y))
print("Çarpım:", carp(x, y))
