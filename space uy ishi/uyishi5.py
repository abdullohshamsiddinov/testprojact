score = 0

answer = input("1. Qaysi hayvon Xitoyning ramzi?: ")
if answer.lower() == "qo'ng'iroq":
    score += 1

answer = input("2. Zebra qayerda yashaydi?: ")
if answer.lower() == "afrika":
    score += 1

answer = input("3. Turna qaysi davlat ramzi hisoblanadi?: ")
if answer.lower() == "mexico":
    score += 1

answer = input("4. Kanguru jangoboz hayvonlariga kiradi (ha/yo'q): ")
if answer.lower() == "ha":
    score += 1

answer = input("5. Qaysi hayvon Dunyo Xaritasi ramzi bo'lmagan?: ")
if answer.lower() == "quyon":
    score += 1

print("Yakuniy ballingiz:", score)
print("Berilgan", score, "savolga to'g'ri javob berildi.")
