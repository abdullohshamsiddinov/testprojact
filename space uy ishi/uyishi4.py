# Birinchi o'yinchining tanlovini qabul qilish
player1_choice = input("Birinchi o'yinchining tanlovini kiriting (tosh/qaychi/qog'oz): ")

# Ikkinchi o'yinchidan tanlovni so'raladi
player2_choice = input("Ikkinchi o'yinchining tanlovini kiriting (tosh/qaychi/qog'oz): ")

# O'yin natijasini aniqlash va xabar chiqarish
if player1_choice == player2_choice:
    print("Durrang!")
elif (
    (player1_choice == "tosh" and player2_choice == "qaychi") or
    (player1_choice == "qaychi" and player2_choice == "qog'oz") or
    (player1_choice == "qog'oz" and player2_choice == "tosh")
):
    print("Birinchi o'yinchi g'olib bo'ldi!")
else:
    print("Ikkinchi o'yinchi g'olib bo'ldi!")
