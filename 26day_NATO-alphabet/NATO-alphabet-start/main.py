# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_data = data.iterrows()
nato_datas_dic = {row.letter: row.code for index, row in nato_data}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = list(input("Enter a word: ").upper())
result = [nato_datas_dic[letter] for letter in word]
print(result)
