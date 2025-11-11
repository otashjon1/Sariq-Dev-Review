

names=['java', 'Kamro', 'Mansu', "Sarik", 'Otash']

for name in names:
    print("hello" +' '+ name)
length=str(len(names))
print("Kod"+" "+ length + " "+" marta takrorlandi!")

toq_sonlar=list(range(11, 100 , 2))
print(toq_sonlar)

for kubi in toq_sonlar:
    print(kubi**3)
kinos=[]
for kino in range(5):
    user_movie=input(f"what is your {kino+1} favorite movies?\n")
    kinos.append(user_movie)
print(f"Your fav movies: {kinos}")

their_names=[]
suxbatdosh=int(input("Bugun nechta odam bilan suxbatlashdingiz?"))
for x in range(suxbatdosh):
    names=input(f"{x+1}-ning ismi nima edi?")
    their_names.append(names)

print(their_names)