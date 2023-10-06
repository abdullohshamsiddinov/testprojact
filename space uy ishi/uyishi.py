#list boicha vazifa
royxat = []

royxat.append(2)
royxat.append(5)
royxat.append(8)
royxat.append(3)
royxat.append(1)

yigindi = sum(royxat)
print(yigindi)

#List indekslash vazifasi:



nomlar = ["Ali", "Vali", "Hasan", "Husan", "Ahmad"]

uchinchi_nom = nomlar.pop(2)
print(uchinchi_nom)
print(nomlar)

#List elementining qiymatini o‘zgartirish topshirig‘i:

ranglar = ["qora", "oq", "yashil", "sariq", "ko'k"]

ranglar[1:6] = ["to'q sariq"]

print(ranglar)

#Tuple uchun vazifa:

my_tuple = ("olma", 15, 4.5, True, [1, 2, 3])

ikkinchi_element = my_tuple[1]
print(ikkinchi_element)

#List birlashtirish vazifasi:

royxat1 = [1, 2, 3]
royxat2 = [4, 5, 6]

birgina_royxat = royxat1 + royxat2

print(birgina_royxat)
#List elementni qidirish vazifasi:

raqamlar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if 7 in raqamlar:
    print("Ro'yxatda 7 raqami bor!")
else:
    print("Ro'yxatda 7 raqami yo'q!")

#List uchun vazifa:
raqamlar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

dastlabki_uchta_raqam = raqamlar[:3]
print(dastlabki_uchta_raqam)

oxirgi_uchta_raqam = raqamlar[-3:]
print(oxirgi_uchta_raqam)
