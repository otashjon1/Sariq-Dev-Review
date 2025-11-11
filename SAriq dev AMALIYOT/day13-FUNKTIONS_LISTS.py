

#Matnlardan iborat ro'yxat qabul qilib,
#ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.

#
# def title_names(name):
#     for x in range(len(name)):
#         name[x]=name[x].title()
#     return name
# names=['otabek', 'mansur', 'kamron', 'javokhir']
# print(title_names(names))


#Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring

#
# def title_names(name):
#     for x in range(len(name)):
#         name[x]=name[x].title()
#     return name
# names=['otabek', 'mansur', 'kamron', 'javokhir']
# new_names=names
# print(names)
# print(title_names(new_names))




#Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan
# va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.



# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#             ism = ismlar.pop()
#             baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#             baholar[ism]=baho
#     return baholar
#
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)

#
# def bahola(ismlar):
#     baholar = {}
#     for x in range(len(ismlar)):
#             ism = ismlar[x]
#             baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#             baholar[ism]=baho
#     return baholar
#
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)

