


"Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing"


def kopaytr(*sonlar):
    yigindi=1
    for son in sonlar:
        yigindi*=son
    return yigindi
print(kopaytr(3,4,2,3))


#Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning ismi va familiyasi majburiy argument,
# qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def students(name, surname, **informations):
    return f"This student is {name}, {surname} {informations}"

student1=students('Otaabek', 'Rayimkulov' , yil=2004, bros='Muahammad' )
print(student1)