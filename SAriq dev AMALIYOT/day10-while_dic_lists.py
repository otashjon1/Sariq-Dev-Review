"""

Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
"""

mix_goods=[]
finish=True
while finish:
    survay=input("What is this prduct? (type 'stop' if the goods are finished. )")
    if survay!="stop":
        mix_goods.append(survay)

    else:
        finish=False
print(mix_goods)
"""
e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang."""
e1_bozor={}
finish=True
while finish:
    goods=input("Put the good. (type the 'stop' if you done.)")
    if goods=="stop":
        finish=False
    else:
        costs=input("How much is it")
        e1_bozor[goods]=costs

print("\nE-market goods with costts")
for product, cost in e1_bozor.items():
    print(f"{product.title()}'s cost is: {cost}")


"""
Yuqoridagi ikki dasturni jamlaymiz. 
Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring 
(tayyor ro'yxat ishlatishingiz mumkin). 
Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda 
"Bizda bu mahsulot yo'q" degan xabarni kor'sating."""

for mix in mix_goods:
    if mix in e1_bozor:
        print(f"{mix}'s cost is: {e1_bozor[mix]}")
    if mix not in e1_bozor:
        print(f"Sorry, we do not have this {mix} product")