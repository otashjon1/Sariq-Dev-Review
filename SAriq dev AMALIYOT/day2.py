

countries=['Uzbekistan', 'America', 'England', 'Egypt', 'Australia', 'New Zealand']
print(countries)
print(len(countries))
print(sorted(countries))
countries.sort(reverse=True)
print(countries)
juft_sonlar=list(range(120, 1201, 2))
print(juft_sonlar)
print(sum(juft_sonlar))
eng_katta=max(juft_sonlar)
eng_kichiki=min((juft_sonlar))
print(eng_katta-eng_kichiki)
print(len(juft_sonlar))
#for x in range(120, 1201, 2):
#    print(x)

print("Boshi:", juft_sonlar[:20])
middle_index = len(juft_sonlar) // 2
print("O'rtasi:", juft_sonlar[middle_index-10:middle_index+10])
print("Oxiri:", juft_sonlar[-20:])

taomlar=["Osh", "Shashlik", "sho'rva", "Manti", "Chuchvara " ]
print(taomlar)
nonushta=["Tea", "Shashlik", "sho'rva", "cofee", "Chuchvara " ]
print(nonushta)
my_tuple=tuple(nonushta)
nonushta[0]= "choy va shakar"
print(my_tuple)

