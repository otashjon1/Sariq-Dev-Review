

otam={
   "Name": "Dadamning ismi Ilkhomjon.",
   "Birthday": "1975 yilda tug'ilgan.",
   "Live_place": "Hozirda Jizzakh tumanida yashab kelmoqda"

}
print(otam['Name'])
print(otam['Birthday'])
print(otam['Live_place'])

family={
   "Otabek": "Otabek's favorite food is Osh",
   "Muhammad": "Muhammad's favorite food is Kebab",
   "Doniyor": "Doniyor's favorite food is Somsa"
}

print(f"{family["Otabek"]}. \n{family["Muhammad"]}. \n{family["Doniyor"]}.")

python_dict={
   "Integer": "Integer is used for change the string to integer",
   "Float": "Float is used for change the string to float",
   "len": "Len helps to count the number of values",
   "Input": "Input helps to ask the question from the user"
}

print(f"{python_dict["Integer"]}. \n{python_dict["Float"]}.\n{python_dict["len"]}.\n{python_dict["Input"]}")

random_dict=input("Write the one dictionary").title()

if random_dict in python_dict:
   print(python_dict[random_dict])
if random_dict not in python_dict:
   print("This word is not available in dict")

eng_uzb={'apple': 'olma', 'banana': 'banan', 'pineapple': 'ananas'}
print(eng_uzb.get('apple', 'This fruit is not available'))
print(eng_uzb.get('melon', 'This fruit is not available'))
