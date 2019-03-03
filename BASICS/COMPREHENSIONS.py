#NOTE - LIST COMPREHENSION -
#QUESTION 1 - LIST OF WORDS FROM A PRAGRAPH
paragraph = ["There was a fox.", "It was brown in color.", "It was seen near the farm sometimes back."]

#problem with split is that it creates a list of the split items. SO we are getting a list of lists, instead of list of the words in this case.
single_word_list = [sentence.split() for sentence in paragraph]
print(single_word_list)

single_word_list = [word for sentence in paragraph for word in sentence.split() ]
print(single_word_list)

#QUESTION 2 - LIST OF WORDS STARTING WITH A VOWEL IN A PRAGRAPH

vowels = ['a','e','i','o','u']
single_word_list = [word for sentence in paragraph for word in sentence.split() if word[0].lower() in vowels]
print(single_word_list)

#NOTE - DICTIONARY COMPREHENSION
squared_dict = {n:n*n for n in range (25)}
print(squared_dict)

#NOTE - Handling categorical variables using dict comprehension
varlist =  ['is_gas', 'is_turbo', 'is_2_doors', 'is_front_eng']
# Applying the function to the housing list
carPrice[varlist[0]] = carPrice[varlist[0]].apply(lambda x: 1.0 if (x=='gas') else 0.0)
carPrice[varlist[1]] = carPrice[varlist[1]].apply(lambda x: 1.0 if (x=='turbo') else 0.0)
carPrice[varlist[2]] = carPrice[varlist[2]].apply(lambda x: 1.0 if (x=='two') else 0.0)
carPrice[varlist[3]] = carPrice[varlist[3]].apply(lambda x: 1.0 if (x=='front') else 0.0)
carPrice.info()
#Here is the list comprehension 
carPrice = carPrice.astype({var:"float" for var in varlist})

#NOTE - DECISION IN COMPREHENSION
l = [22, 13, 45, 50, 98, 69, 43, 44, 1]
[x+1 if x >= 45 else x+5 for x in l ]
#NOTE another way -
num_list = [value for value in y if value]
