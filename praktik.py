'''Робота з текстами'''
from re import sub

text = "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."

reg_exp = r'[^a-zA-Z0-9 ]' 
normalized_text = text.lower()
normalized_text = sub(reg_exp, '', normalized_text)

words_list = normalized_text.split()
unique_words_list = set(words_list)
n_words = len(words_list)
n_unique_words = len(unique_words_list)

words_quantity = {}

for word in unique_words_list:
    words_quantity[word] = normalized_text.count(word)

words_quantity_list = list(words_quantity.items())

def sort_by_quantity(element):
    return element[1]

words_quantity_list.sort(key=sort_by_quantity, reverse=True)

# print(n_words)              
print(words_quantity_list)   # виведення відсортованого теексту з кількістю повторюваності 