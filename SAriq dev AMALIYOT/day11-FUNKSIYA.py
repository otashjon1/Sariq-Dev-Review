
# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

# def user():
#     name=input("What is your name?")
#     age=int(input("How old are you?"))
#     birth=2025-age
#     print(f"{name} is {age} years old. You were born in {birth}-year.")
# user()



# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

# def kv_kub(number):
#     kv=number**2
#     kub=number**3
#     return f"{number}ning kvadrati {kv} ga, {number}ning kubi {kub} ga teng."
# son=int(input("Enter the number"))
# print(kv_kub(son))


# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing
# def num(number):
#     if number%2==0:
#         return f"Sizning {num1} is juft son"
#     else:
#         return f"Sizning kiritgan {num1} raqamiz toq son"
#
# num1=int(input("Biror son kiriting"))
# print(num(num1))



# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
#
# def two_number(num1, num2):
#
#     if num1>num2:
#         return f"{num1}>{num2}"
#     elif num1<num2:
#         return f"{num1}<{num2}"
#     else:
#         return f"{num1}={num2}"
# num=1
# num1=int(input(f"{num}-Enter two number"))
# num2=int(input(f"{num+1}-Enter two number"))
#
# print(two_number(num1, num2))


# Foydalanuvchidan x va y sonlarini olib,
# x y (y-xning darajasi holatida yozilgan)ni konsolga chiqaruvchi funksiya yozing.

# def x_y_numbers(num1, num2):
#     return f"{num1**num2}"
# x=int(input("Enter the number for x"))
# y=int(input("Enter the number for y"))
# print(x_y_numbers(x,y))



# Foydalanuvchidan son qabul qilib,
# sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing.
# Natijalarni konsolga chiqaring

def number(num):
     for n in range(2,11):
         if num%n==0:
            print(f"{num} sonining 2 dan 10 gacha qoldiqsiz bo'linadigan son: {n}")

user_num=int(input("Enter the number."))
number(user_num)