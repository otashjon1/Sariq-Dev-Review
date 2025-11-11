
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

for car in cars:
    if car !="gm":
        print(car.title())
    else:
        print(car.upper())

for car in cars:
    if car =="gm":
        print(car.upper())
    else:
        print(car.title())


login=input("Ismingizni kirting")
if login=="Admin":
    print(f"Xush kelibsiz {login}, foydalanuvchilar ro'yxatini ko'rishni xoxlaysizmi?")
else:
    print(f"Xush kelibsiz, {login}")

son1=input("Birinchi sonni kiriting.\n")
son2=input("Ikkinchi sonni kiriting.\n")

if son1==son2:
    print("Siz kiritgan son teng ekan.")
else:
    print(f"Siz shu sonlarni kiritdingiz: {son1}, {son2}")

istalgan_son=int(input("Istalgan sonni kiriting.\n"))
if istalgan_son >=0:
    print("Siz musbat son kiritdingiz")
else:
    print("Siz manfiy son kiritdingiz.")

ildizi=float(input("Musbat son kiriting.\n"))
if ildizi>=0:
    print(f"Siz kiritgan sonning ildzi {ildizi**0.5} ga teng.")
else:
    print("Musbat son kiriting")