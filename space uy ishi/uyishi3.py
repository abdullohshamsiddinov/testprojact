# "total" o'zgaruvchisini 0 ga tenglash
total = 0

# Foydalanuvchidan raqamlarni kiritish uchun for tsiklidan foydalanish
for i in range(5):
    number = int(input("Raqamni kiriting: "))
    total += number

# Barcha raqamlarning yig'indisini chop etish
print("Raqamlar yig'indisi:", total)
