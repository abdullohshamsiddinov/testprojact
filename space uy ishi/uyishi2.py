import random

# 1 dan 10 gacha bo'lgan bir sonni generatsiya qilish
maxfiy_raqam = random.randint(1, 10)

# Tahminlar soni
tahminlar = 0

# For tsikli va input() funksiyasidan foydalanib raqamni taxminlash
for i in range(3):
    tahmin = int(input("Raqamni toping (1 dan 10 gacha): "))
    tahminlar += 1
    
    if tahmin == maxfiy_raqam:
        print("Tabriklaymiz! Siz", tahminlar, "urinishdagi raqamni topdingiz!")
        break
    elif tahmin < maxfiy_raqam:
        print("Yashirin raqam kattaroq")
    else:
        print("Yashirin raqam kichikroq")

# O'yin tugadi
print("O'yin tugadi!")
