#
#

#
#
#
# son=0
# while son <5:
#     print(son, end='')     end=' ' -ning vazifasi sonlarni bitta qatorga chiqaradi alohida qatorga emas.
#     son+=1
# print("dastur yakunlandi")
#




# """1- Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
#  Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating"""
#
#
#
#
# books=[]
# while True:
#     fav_book = input("What is your favorite books?")
#     if fav_book=="stop":
#         break
#     books.append(fav_book)
# print(f"Your fav books are {books}")
# print("Thanks for sharing your books")


"""
Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq:
7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm,
65 dan kattalarga bepul. Shunday while tsikl yozingki,
dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

"""

# while True:
#     age=input("Please select your age. (type the 'quit' to stop)")
#
#     if age=="quit":
#         break
#     age=int(age)
#     if age<7:
#         print("The ticket price is 2$")
#     elif age>=7 and age<19:
#         print("The ticket price is 5$")
#     elif age>=19 and age<65:
#         print("The ticket price is 7$")
#     elif age> 65:
#         print("The ticket price is 10$")





"""Shartni while ichida tekshirishShartni while ichida tekshirish"""

# yosh = ""
# while yosh not in ["exit", "quit"]:
#     yosh = input("Yoshingizni kiriting (yoki 'exit' yoki 'quit' deb yozing): ")
#
#     if yosh.lower() in ["exit", "quit"]:
#         print("Dastur tugatildi. Rahmat!")
#         break
#
#     yosh = int(yosh)
#     if yosh < 7:
#         print("Chipta narxi 2000 so‘m.")
#     elif yosh < 18:
#         print("Chipta narxi 3000 so‘m.")
#     elif yosh < 65:
#         print("Chipta narxi 10000 so‘m.")
#     else:
#         print("Sizga chipta bepul!")

"""Quyidagi dasturda bir nechta mantiqiy xatolar bor. 
Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
"""
#
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif  float(qiymat)<0:
#         continue      #break va continue ning farqi continue siklning bowiga qaytib yana kod ishlaydi
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
