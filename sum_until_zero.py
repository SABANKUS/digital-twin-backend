# sum_until_zero

total = 0
while True:
    n = float(input("Bir sayi gir (0 girersen bitir): "))
    if n == 0:
        break
    
    total += n

print("Girilen sayilarin toplami: ", total)

