# functions.py

def selamla(isim):
    """Verilen isme göre selam verir."""
    return f"Merhaba, {isim}!"

def topla(a, b):
    """İki sayinin toplamini döndürür."""
    return a + b

def carp(a, b):
    """İki sayının çarpımını döndürür."""
    return a * b

# Bu kısım functions.py doğrudan çalıştırıldığında devreye girer
if __name__ == "__main__":
    print(selamla("Dijital İkiz"))
    print("3 + 7 =", topla(3, 7))
    print("5 * 9 =", carp(5, 9))
