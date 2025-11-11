ismlar=['Kamron', 'Mansur', 'Javoxir']
print(ismlar)

xabar1="Qalesan"
xabar2="Qayerdasan"
xabar3="Ishdamisan?"

print(ismlar[0] +' '+ xabar1)
print(ismlar[1] +' '+ xabar2)
print(ismlar[2] +' '+ xabar3)

sonlar=[10, -12, 3.4]

sonlar[2]=3
print(sonlar[0]+ 13)
print(sonlar[1]+ 112)
print(sonlar[2]** 2)

t_shaxslar=['Amir Temur', 'Cholpon']
z_shaxslar=['Umidjon', 'Azam']
t_shaxslar.pop(1)
z_shaxslar.pop(1)

print(f"Man tarixiy shaxslardan " + str(t_shaxslar)+ " bilan, zamonaviy shaxslardan esa " + str(z_shaxslar) + " bilan uchrashishni hoxlayman!" )

friends=[]
print(friends)
friends.append('bobur')
friends.append('Doni')
friends.append('Quchqor')
friends.append('Avaz')
chaqirmoqchilarim=friends
print(chaqirmoqchilarim)

kelmaydiganlar='Doni'
kelmaydiganlar_dostlar=kelmaydiganlar
print(f"Kelmaydigan do'stlarim: {kelmaydiganlar_dostlar}")
keladigonlar=friends.remove(kelmaydiganlar_dostlar)
print(f"Keladiganlar: {friends}")

