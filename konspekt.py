'''Що робити, якщо нам потрібен текст із перенесенням рядків (коли в тексті більше одного рядка)? 
Для цього можна скористатися потрійним повторенням лапок:'''

# text = """This is first line
# And second line
# Last third line"""
# або
# one_line_text = "Textual data in Python is handled with str objects, or strings. "\
#                 "Strings are immutable sequences of Unicode code points. "\
#                 "String literals are written in a variety of ways: single quotes, double quotes, triple quoted."

'''Python сприймає рядкові змінні, між якими немає нічого, крім пробілів та/або символів нового рядка, як один рядок:'''

# ("spam " "eggs") == "spam eggs"  # True

