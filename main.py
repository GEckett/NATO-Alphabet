import pandas

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

nato_alpha = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(nato_alpha)
df_dict = {row.letter: row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Enter a word").upper()
user_word_nato = [df_dict[letter] for letter in user_word]
print(user_word_nato)
