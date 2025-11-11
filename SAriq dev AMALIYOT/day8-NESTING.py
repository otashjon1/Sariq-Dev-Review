#
#  Nesting- nimanidir ichida nimadir saqlash. Misol uchun lug'at ichida list yoki list ichida lug'at saqlash
# fam_net_per1={
#     "name": "Azam",
#     "Job": "teacher",
#     "Place": "Tashkent",
#     "Achievments": "Azam-school"
# }
#
#
# fam_net_per2={
#     "name": "Mirshakar",
#     "Job": "Comedian",
#     "Place": "Tashkent",
#     "Achievments": "Konserts-Chempion, Maladest"
# }
#
# fam_net_per3={
#     "name": "Konsta",
#     "Job": "Rapper",
#     "Place": "Tashkent",
#     "Achievments": "Konserts-Insonlar, Ota"
# }
#
# fam_net_per4={
#     "name": "Doston",
#     "Job": "Sportsman",
#     "Place": "Fargana",
#     "Achievments": "MMA Chempion, Wrestling Chempion"
# }
#
# famous_people=[fam_net_per1, fam_net_per2, fam_net_per3, fam_net_per4]
#
# for x in famous_people:
#     print(f"{x["name"]} is a {x["Job"]}.\n"
#           f"{x["name"]} lives in {x["Place"]}.\n"
#           f"{x["name"]} achieved these: {x["Achievments"]}.")
#
# Ali_movie=[]
# for x in range(3):
#     person1=input("Ali which movies do you like?")
#     Ali_movie.append(person1)
#
# Vali_movie=[]
# for x in range(3):
#     person2=input("Vali which movies do you like?")
#     Vali_movie.append(person2)
#
# Otabek_movie=[]
# for x in range(3):
#     person3=input("Otabek which movies do you like?")
#     Otabek_movie.append(person3)
#
# family_members={
#     "Ali": Ali_movie,
#     "Vali": Vali_movie,
#     "Otabek": Otabek_movie
# }
#
# print(f"Alining sevimli kinolari: {family_members["Ali"]}\n"
#       f"Valining sevimli kinolari: {family_members["Vali"]}\n"
#       f"Otabekning sevimli kinolari: {family_members["Otabek"]}")



countries={
    "USA":{
        "Area": "9,826,675 km²",
        "People": "347",
        "Currency": "US dollor"
    },
    "Uzbekistan":{
        "Area": "448,978 km²",
        "People": "37",
        "Currency": "Sum"
    },
    "China": {
        "Area": "9,388,211 km²",
        "People": "1.416",
        "Currency": "Chinese yuan"
    },
    "Germany":{
        "Area": "357,000-360,000 km²",
        "People": "84",
        "Currency": "EURO"
    }

}

for country in countries:
    print(f"General information about {country}\n"
          f"The area: {countries[country]["Area"]}.\n"
          f"People: {countries[country]["People"]} million.\n"
          f"Currency: {countries[country]["Currency"]}")


asking=input("Choose the country.")
if asking in countries:
    print(f"General information about {asking}\n"
          f"The area: {countries[asking]["Area"]}.\n"
          f"People: {countries[asking]["People"]} million.\n"
          f"Currency: {countries[asking]["Currency"]}")
else:
    print("Sorry, we do not have any information about this country.")