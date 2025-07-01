# calculator.py
a = float(input("Birinci sayiyi gir: "))
b = float(input("İkinci sayiyi gir: "))

toplam = a + b
fark = a - b
carpim = a * b
bolum = a / b if b != 0 else "Tanimsiz (b sifir)"

print("Toplam: ", toplam)
print("Fark: ",fark)
print("Çarpim: ", carpim)
print("Bölüm: ",bolum)
