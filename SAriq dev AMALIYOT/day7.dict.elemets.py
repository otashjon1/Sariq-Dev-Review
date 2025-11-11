#
#
# python_dict={
#     'for': 'it is hepls to do something again again and again',
#     'if': 'it checks the conditions',
#     'boolean': 'it is logically value',
#     'float': 'it is the whole number'
# }
#
# for x in sorted(python_dict):
#     print(x, ":",python_dict[x])
#
#
#
# coun_capital={
#     "Afghanistan": "Kobul",
#     "Uzbekistan": "Tashkent",
#     "Azerbaijan": "Baku",
#     "Australia": "Canberra",
#     "USA": "Washington"
# }
# print("Dunyo davlarlari.")
# for key in sorted(coun_capital):
#     print(f"{key}!")
# print("Dunyo poytaxtlari.")
# for value in sorted(coun_capital.values()):
#     print(f"{value}!")
#
# survey=input("which country's capital do you want to know?")
# if survey in coun_capital.keys():
#     print(coun_capital[survey])
# else:
#     print("Sorry, we do not have any information about this!")
#
#

# Menu={
#     "Plov": "10$",
#     "Shashlik": "13$",
#     "Samsa": "15$",
#     "Manti": "17$",
#     "Gilmindi": "20$",
# }
# print("Please, order 3 food")
# orders=[]
# for x in range(3):
#     order=input(f"Please order {x+1}- food. What would you like to eat?")
#     orders.append(order)
# for order in orders:
#     if order in Menu:
#         print(f"{order}: {Menu[order]}")
#     else:
#         print(f"Sorry, we do not have {order}")