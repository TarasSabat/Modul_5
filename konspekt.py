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

'''Невидимі (керуючі) символи. Застосування'''

# carriage return

# print('testNew string', end='\n\t')
# print('Hello world',)

'''Напишіть програму, яка приймає від користувача рядок і підстроку, а потім визначає позицію (індекс) першого входження підстроки у рядок. # Якщо підстрока не знайдена, програма повинна повідомити користувача про це. 
Метод find - виводить індекс початку першого збігу в рядку, якщо не знайде збігів то поверне -1
S.find(str, [start], [end]) '''

# main_string = input("Введіть рядок: ")
# substring = input("Введіть підстроку для пошуку: ")
# index = main_string.find(substring)
# if index != -1:
#     print(f'Підстрока знайдена на позиції: {index}')
# else:
#     print(f'Підстрока не знайдена')

'''Метод rfind - виводить індекс початку першого збігу в рядку з права на ліво, якщо не знайде збігів то поверне -1 
S.rfind(str, [start], [end])'''

# s = 'Some words'
# print(s.rfind('o'))

'''Дано рядок символів. Виключити з цього рядка групи символів між дужками [, ]. Самі дужки теж мають бути виключені. Передбачається, що в кожній парі дужок немає інших дужок.'''

# string = 'Виключити з цього [рядка групи] символів, [розташовані між] дужками [, ].'
# # Виключити з цього символів, дужками.
# # 1 ітерація циклу-> Виключити з цього  символів, [розташовані між] дужками [, ].
# # 2 ітерація циклу-> Виключити з цього  символів,  дужками [, ].
# # 3 ітерація циклу-> Виключити з цього  символів,  дужками .

# start_index = string.find('[')
# end_index = string.find(']')

# new_string = string[:start_index] + string[end_index + 1:]
# print(new_string)

# def sanitize(string):
#     new_string = string[:]  # копія строки
#     while True:
#         start_index = new_string.find('[')
#         end_index = new_string.find(']')
#         if start_index == -1:
#             break
#         new_string = new_string[:start_index] + new_string[end_index+1:]
#     return new_string

# print(sanitize(string))

"""
Метод: isdigit
​
Різниця між isdigit(), isnumeric() and isdecimal()
+-------------+-----------+-------------+-------------------------------------+
| isdecimal() | isdigit() | isnumeric() |          Example                    |
+-------------+-----------+-------------+-------------------------------------+
|  True       |    True   |    True     | "038", "੦੩੮", "０３８"              |
|  False      |    True   |    True     | "⁰³⁸", "🄀⒊⒏", "⓪③⑧"                |
|  False      |   False   |    True     | "↉⅛⅘", "ⅠⅢⅧ", "⑩⑬㊿", "壹貳參"    |
|  False      |   False   |   False     | "abc", "38.0", "-38"                |
+-------------+-----------+-------------+--------------------------------------+
1. Знайти кількість цифр у рядку
2. Знайти кількість чисел у рядку
"""

# string = "Нільс Бор народився в родині професора фізіології Копенгагенського університету Християна Бора(1858-1911), " \
#          "й Еллен Адлер (1860-1930). Батьки Бора одружилися 1881 року. Батька Нільса Бора двічі висували кандидатом " \
#          "на Нобелівську премію з фізіології або медицини[6]. Мати була донькою впливового та вельми заможного " \
#          "єврейського банкіра і парламентаря-ліберала Давида Баруха Адлера[da] (1826-1878) і Дженні Рафаел (1830-1902) " \
#          "із британської єврейської банкірської династії Raphael Raphael & sons[en][7]."

# def count_digits(string):
#     count = 0
#     for element in string:
#         if element.isdigit():
#             count += 1
#     return count

# print(count_digits(string))

# def count_numbers(string):
#     count = 0
#     position = 0
#     nums = []
#     while position < len(string):
#         if string[position].isdigit():  # початок числа
#             num = ''
#             while position < len(string) and string[position].isdigit():  # шукаємо закінчення числа
#                 num += string[position]  # записуємо число
#                 position += 1  # збільшуємо позицію на 1
#             nums.append(num)   # додаємо знайдене число до списку
#             count += 1  # збільшуємо лічильник на 1
#         else:
#             position += 1  # збільшуємо позицію на 1
#     return count, nums  # повертаємо кортеж

# print(count_numbers(string))

"""
Метод: isdigit
----
Заданий список, кожним елементом якого є рядок символів, що складається з одних цифр.
Впорядкувати елементи масиву за зростанням їх числових значень і вивести на екран.
Від максимального елемента відняти значення мінімального та вивести різницю на екран.
Підрахувати середнє значення всіх елементів.
"""
# numbers = ['124', '465', '321', '55', 'abc', '211c', '-3']

# def sanitaze(data):
#     result = []
#     for element in data:
#         if element.isdigit():
#             result.append(element)
#     return result


# def transform_to_numbers(data):
#     result = []
#     for element in data:
#         result.append(int(element))
#     return result

# san_nums = sanitaze(numbers)
# print(sorted(san_nums))
# san_nums = transform_to_numbers(san_nums)
# san_nums.sort()
# print(san_nums)
# print(max(san_nums) - min(san_nums))
# print(sum(san_nums) / len(san_nums))

"""
Методи: split, join
----
Розбираємо URL з Rozetka
"""
# url_query = 'producer=apple;series=iphone-14-pro;41404=256-gb1261112'
# query = url_query.split(';')   # розділяємо по ';'
# print(query)
# ob_query = {}
# for element in query:
#     key, value = element.split('=')
#     ob_query.update({key: value})
# print(ob_query)

# result = []
# for key in ob_query:            # зворотня операція
#     result.append(key + '=' + ob_query[key])
# print(';'.join(result))

"""
Методи: split, replace - заміняє 'щось1' на 'щось2'
Коли нам треба замінити деякий підрядок у рядку ми можемо скористатися методом replace:

message = "У темній кімнаті всі кішки чорні (мабуть)"
square_brackets = message.replace("(", "[").replace(")", "]")
clear_brackets = message.replace("(", "").replace(")", "")

print(square_brackets)  # У темній кімнаті всі кішки чорні [мабуть]
print(clear_brackets)  # У темній кімнаті всі кішки чорні мабуть
Для видалення фіксованої послідовності на початку рядка є метод removeprefix:

print('TestHook'.removeprefix('Test'))  # Hook
print('TestHook'.removeprefix('Hook'))  # TestHook
Є парний метод для видалення послідовності в кінці рядка, removesuffix:

print('TestHook'.removesuffix('Hook'))  # Test
print('TestHook'.removesuffix('Test'))  # TestHook
----
Парсимо query запит для google. Тут класичний роздільник & і перетворюємо на словник із даними
"""
# url_search = 'https://www.google.com/search?q=cat+and+dogs&oq=cat+and+dog'
# _, query = url_search.split('?')
# print(query)
# obj_query = {}
# for el in query.split('&'):
#     key, value = el.split('=')
#     obj_query.update({key: value.replace('+', ' ')})
# print(obj_query)

"""
Методи: strip, removeprefix, replace, format
Щоб видалити пропуски у правого краю рядка, використовують метод rstrip:

name = "Avril Lavigne        "
print(name.rstrip())  # Avril Lavigne
Щоб видалити пропуски біля лівого краю рядка, використовують метод lstrip:

name = "         Avril Lavigne"
print(name.lstrip())  # Avril Lavigne
Щоб видалити пропуски з обох боків рядка, використовують метод strip:

name = "         Avril Lavigne          "
print(name.strip())  # Avril Lavigne
------
Провести валідацію списку телефонів
Телефон: +380501234567 Де: +380 код країни телефон 501234567
Вважаємо, що телефон валідний з кодом і без коду
"""
# phone_storage = ["380669640547", "0637306465 ", " 380961935171", "632643973", "050832520 ", "000000000", "48730283918",
#                  "986223575", "375297947963", "+38(050)123-32-34", "38(050)123 32 34", "38(050)123 32 3b"]

# codes_operators = {"067", "068", "096", "097", "098", "050", "066", "095", "099", "063", "073", "093"}

# def sanitize_phone(phone: str) -> str:
#     new_phone = (phone.strip()
#                  .lstrip('+') # або 
#                  # .removeprefix('+')
#                  .replace('(', '')
#                  .replace(')', '')
#                  .replace(' ', '')
#                  .replace('-', '')
#                  )
#     return new_phone


# def is_valid_phone(phone: str) -> bool:
#     def is_valid_operator(phone: str) -> bool:
#         if phone[:3] in codes_operators:
#             return True
#         return False

#     if phone.isdigit():
#         if len(phone) == 12:
#             if phone[:2] == '38':
#                 return is_valid_operator(phone[2:])
#         elif len(phone) == 10:
#             return is_valid_operator(phone)
#     return False

# if __name__ == "__main__":
#     for phone in phone_storage:
#         phone = sanitize_phone(phone)
#         if is_valid_phone(phone):
#             print('Phone: {:>12} is valid'.format(phone))
#         else:
#             print('Phone: {:>12} is invalid'.format(phone))

"""
Метод translate

Метод translate у Python дозволяє замінити символ у рядку на інший з карти (таблиці) відповідності, котру можна задати. Якщо ми використовуємо словник, ми повинні використовувати ASCII коди замість символів.

Приклад:
replace_dict = {117: "o"}
txt = "sun"
print(txt.translate(replace_dict))  # son
Що сталося? Ми замінили в тексті символ "u" на символ "o". Значення 117 — це ASCII код символу 'u', яке, як знаємо, можна отримати з допомогою функції ord("u").

replace_dict = {ord("u"): "o"}
txt = "sun"
print(txt.translate(replace_dict))  # son
Таким чином translate() – метод, який повертає рядок, де деякі задані символи замінюються на символи, описані у словнику, або таблиці відображення. Якщо символ не вказано у словнику/таблиці, символ не буде замінено. Для створення таблиці відображення використовується метод maketrans.

txt = "sun"
my_table = txt.maketrans("u", "o")
print(txt.translate(my_table))  # son
Можна визначити набір для замін

txt = "sun"
my_table = txt.maketrans("nus", "mot")
print(txt.translate(my_table))  # tom
Третій параметр у таблиці зіставлення описує символи, які ви хочете видалити з рядка:

txt = "the sun"
my_table = txt.maketrans("nus", "nos", "he t")
print(txt.translate(my_table))  # son
Якщо ми збираємося транслювати кирилицю на латиницю, у нас може виникнути проблема, наприклад, при транслітерації слова "чаша", яке має бути "chasha" і має довжину на два символи більше. Використання maketrans викличе помилку. Як бути?

Для цього можна використовувати вбудовану функцію zip, яка перетворює численні об'єкти, що ітеруються в єдиний об'єкт кортежів, що ітерується, та складається з відповідних елементів:

CYRILLIC = ("а", "ч", "ш")
LATIN = ("a", "ch", "sh")

TRANSLIT_DICT = {}

for c, l in zip(CYRILLIC, LATIN):
    TRANSLIT_DICT[ord(c)] = l
    TRANSLIT_DICT[ord(c.upper())] = l.upper()

print("чаша".translate(TRANSLIT_DICT))  # chasha
print("ЧАША".translate(TRANSLIT_DICT))  # CHASHA
Так швидко можна створити словник для транслітерації. Якщо списки мають різні довжини, то функція zip припинить роботу, щойно закінчиться перший із них.
"""

# data = 'юбщс'
# symbol_map = {
#     ord('ю'): 'u',
#     ord('б'): 'b',
#     ord('щ'): 'shch',
#     ord('с'): 's',
# }

# new_str = data.translate(symbol_map)
# print(new_str)

"""
Метод: Translate
"""

# morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', ord('D'): '-..', ord('E'): '.', 'F': '..-.',
#               'G': '--.', ord('H'): '....', 'I': '..', 'J': '.---', 'K': '-.-', ord('L'): '.-..',
#               'M': '--', 'N': '-.', ord('O'): '---', 'P': '.--.', 'Q': '--.-', ord('R'): '.-.',
#               'S': '...', 'T': '-', 'U': '..-', 'V': '...-', ord('W'): '.--', 'X': '-..-',
#               'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
#               '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#               '8': '---..', '9': '----.'}
# string = 'Hello world'
# data = []
# for ch in string:
#     data.append(ch.upper().translate(morze_dict))
# translated = ' | '.join(data)
# print(translated)


'''
Метод format
------------
< - рівняння по лівому краю
> - рівняння по правому краю
^ - центрування тексту
------------  
Перша цифра у номері пластикової картки означає, до якої платіжної системи вона належить. Усі картки Visa мають
номер, що починається на "4", Mastercard - на "5", а American Express - "3". Якщо картку видала не кредитна
організація, номер може починатися з інших цифр. "1" і "2" - це різні авіалінії, "3" - організації сфери
подорожей та розваг, «6» - мерчендайзингові компанії, «7» - паливні, «8» - підприємства у сфері
телекомунікацій, а «9» - це державні асигнації.
'''
# pay_system = {
#     5: 'MasterCard',
#     4: 'Visa',
#     3: 'American Express'
# }

# card_numbers = ['5375414112345678', '4168757587879876', '216875758787987b']

# def is_valid_card(card):
#     return card.isdigit() and len(card) == 16

# for card in card_numbers:
#     string = 'Номер карти {:,<8} Платіжна система: {:^16} картка валідна: {:>16}'
#     print(string.format(card, pay_system.get(int(card[0]), 'Unknown'), str(is_valid_card(card))))

"""
Метод: format
Будь-яке число можна записати кількома варіантами запису:
- десятковий запис
- двійкове представлення
- шістнадцятиричне представлення
- наукова нотація
- з фіксованою точністю (кількістю знаків після коми) та інші.
Наприклад, вивести числа від 1 до 15 в десятковому, шістнадцятиричному, вісімковому і двійковому уявленні:
for i in range(16):
    s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
    print(s)
Крім того, при створенні рядків буває корисним відформатувати рядок так, щоб знаки на різних рядках були один під одним (додати пробілів), додати заповнення в рядки для того, щоб результат був завжди однієї і тієї ж довжини.
Для таких і подібних завдань в Python вбудована міні-мова форматування рядків .
Або вивести квадрати та куби чисел до 12 у вигляді таблиці, відцентрувавши значення у стовпцях по 10 символів шириною:
width = 5
for num in range(12):
    print('{:^10} {:^10} {:^10}'.format(num, num ** 2, num ** 3))
Мета роботи з метамовою форматування полягає у вказівці у фігурних дужках, яким чином слід перетворити значення перед підстановкою. Форматування працює і з f-рядками, але для більшій читабельності краще скористатися методом format, який приймає як аргументи значення для підстановки в рядок, замість виразів у фігурних дужках.
Самі вирази у фігурних дужках можуть складатися з опису, в якому виді слід вивести число (формат запису, кількість знаків після коми та ін.), і вказівки, чим доповнити рядок (додати пропусків на початку або у кінці, щоб рядок був N знаків завдовжки і т.п.).
---------
Модифікатори
Міні-мова форматування рядків складається з таких модифікаторів, як:
- ім'я поля — необов'язковий елемент, можемо вказати яку саме змінну сюди підставити по її імені:
s = "{name} {last_name}".format(last_name="Dilan", name="Bob")
print(s)  # Bob Dilan
- перетворення — необов'язковий аргумент вказується після символу ! і може бути або r або s. Відповідає за те, чи потрібно спробувати перетворити елемент, або відобразити елемент "як є":
s = "{name!r} {last_name!s}".format(last_name="Dilan", name="Bob")
print(s)  # 'Bob' Dilan
- специфікація вказується після : і відповідає за те, як відобразити значення.
------
Специфікація набагато складніший модифікатор. З її допомогою можна:
змінювати розрядність представлення цілих чисел (десяткові, вісімкові, шістнадцятиричні та ін.);
print('dec: {:d} hex: {:x} bin: {:b}'.format(15, 15, 15))  # dec: 15 hex: f bin: 1111
змінювати точність представлення дробових чисел (округлювати до вказаної кількості знаків);
print('pi: {:0.3}'.format(3.1415))  # pi: 3.14
як відображати знак чисел:
print('"{}" "{:+}" "{:-}" "{: }"'.format(1, 2, -3, 4))  # "1" "+2" "-3" " 4"
як вирівняти положення елементу і чим (якими символами) доповнити;
print("|{:<10}|{:*^10}|{:>10}|".format('left', 'center', 'right'))  # |left      |**center**|     right|
------
Провести валідацію списку телефонів
Телефон: +380501234567 Де: +380 код країни телефон 501234567
Вважаємо, що код валідний з кодом і без коду
"""
# phone_storage = ["380669640547", "0637306465 ", " 380961935171", "632643973", "050832520 ",
#                  "000000000", "48730283918", "986223575", "375297947963", "+38(050)123-32-34", "38(050)123 32 34",
#                  "38(050)123 32 3b"]

# codes_operators = {"067", "068", "096", "097", "098",
#                    "050", "066", "095", "099", "063", "073", "093"}

# from for_import import sanitize_phone, is_valid_phone

# if __name__ == "__main__":
#     print('|{:^14}|{:^12}|'.format('Телефон', 'Результат'))
#     print('|{:^14}|{:^12}|'.format('-' * 13 + ':', ':' + '-' * 10 + ':'))
#     for phone in phone_storage:
#         phone = sanitize_phone(phone)
#         if is_valid_phone(phone):
#             print('|{:>14}|{:^12}|'.format(phone, 'valid'))
#         else:
#             print('|{:>14}|{:^12}|'.format(phone, 'not valid'))

'''
Метод format 
'''
## табличка з числами, числами в квадраті, числами в кубі
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# header = '|{:^15}|{:^15}|{:^15}|'.format('int', 'int^2', 'int^3')
# separator = '-'*len(header)
# body = ''
# for num in numbers:
#     body += '|{:^15}|{:^15}|{:^15}|\n'.format(num, num**2, num**3)
# table = '\n'.join([separator, header, separator, body, separator])
# print(table)

# # табличка з числами в десятковому, шістнадцятиричному, вісімковому і двійковому уявленні
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# header = '|{:^15}|{:^15}|{:^15}|{:^15}|'.format('int', 'dex', 'oct', 'bin')
# separator = '-'*len(header)
# body = ''
# for num in numbers:
#     body += '|{0:^15d}|{0:^15x}|{0:^15o}|{0:^15b}|\n'.format(num)
# table = '\n'.join([separator, header, separator, body, separator])
# print(table)


'''
Метод find 
Метод find приймає три аргументи.

message = "Hello my little friend!"

print(message.find("li", 5, 15))  # 9
print(message.find("li", 10, 15))  # -1
print(message.find("li"))  # 9
Перший аргумент — підрядок, який шукатиме метод find в рядку message, другий аргумент — індекс початку пошуку в message, а третій — індекс закінчення пошуку. Якщо не вказати другий та третій аргумент, то пошук здійсниться по всьому рядку. Метод повертає індекс початку першого збігу у рядку та повертає -1, якщо послідовність не знайдено.
Є аналогічний метод пошуку підрядка в рядку - index. Основна відмінність полягає в тому, що якщо index не знайде підрядок, то викличе виключення ValueError.

message = "Hello my little friend!"

print(message.index("li", 5, 15))
print(message.index("li", 10, 15))

Вивід:
9
Traceback (most recent call last):
  File "e:\WebDir\Works\Python\python-homework-tracks\module-05\src\test.py", line 4, in <module>
    print(message.index("li", 10, 15))
ValueError: substring not found
Якщо вам треба провести пошук підрядка в рядку праворуч, існують методи rfind та rindex:
message = "Hello my little friend!"

print(message.rfind("li"))  # 9
print(message.rindex("li"))  # 9
'''

# files = ['video.avi', 'audio.mp3', 'document.doc', 'folder']
# for file in files:
#     index = file.find('.')    # знаходимо індекси крапок, якщо не знаходить виводить -1
#     suffix = file[index + 1:]    # додаємо 1, щоб суфікс був без папки н.п. .avi
#     print(f'File: {file} Index: {index} Suffix: {suffix}')
   

## або щоб не виводився -1

# files = ['video.avi', 'audio.mp3', 'document.doc', 'folder']
# for file in files:
#     indx = file.find('.')    # знаходимо індекси крапок
#     if indx != -1:
#         suffix = file[indx + 1:]    # додаємо 1, щоб суфікс був без папки н.п. .avi
#         print(f'File: {file} Index: {indx} Suffix: {suffix}')
#     else: 
#         print(f'File: {file} Suffix: not found')

## або з методом index який коли не знаходить символ видає Error 
    
# files = ['video.avi', 'audio.mp3', 'document.doc', 'folder']
# for file in files:
#     try:
#         indx = file.index('.')    # знаходимо індекси крапок
#         suffix = file[indx + 1:]    # додаємо 1, щоб суфікс був без папки н.п. .avi
#         print(f'File: {file} Index: {indx} Suffix: {suffix}')
#     except ValueError:
#         print(f'File: {file} Suffix: not found') 

## якщо файл з двома крапками застосовується метод rindex або rfind

# files = ['video.avi', 'audio.mp3', 'document.doc', 'folder', 'backup.tar.gz']
# for file in files:
#     try:
#         indx = file.rindex('.')    # знаходимо індекси крапок
#         suffix = file[indx + 1:]    # додаємо 1, щоб суфікс був без рапки н.п. .avi
#         print(f'File: {file} Index: {indx} Suffix: {suffix}')
#     except ValueError:
#         print(f'File: {file} Suffix: not found') 

'''
Метод split 
Часто виникає ситуація, коли необхідно розбити рядок на підрядки за деяким символом, наприклад, розбити текст речення по пробілу після точки, або речення за словами. Для цього треба скористатися методом split, який приймає аргумент підрядок-маркер, який буде межею, за якою рядок буде розбитий на частини. В результаті роботи методу повертається список рядків.

message = "Hello, my little friend. Today is a very good day."
words = message.split(" ")
sentences = message.split(". ")
print(words)
print(sentences)
Вивід:

['Hello,', 'my', 'little', 'friend.', 'Today', 'is', 'a', 'very', 'good', 'day.']
['Hello, my little friend', 'Today is a very good day.']

Конкатенація рядків
Всі рядки незмінні, тому всі методи, які якось "модифікують" рядки, повертають нові рядки, ніяк не змінюючи оригінальний рядок.
Для об'єднання кількох рядків в один через деякий роздільник використовується метод join. По суті це операція зворотна split:

words = [
    "Hello,",
    "my",
    "little",
    "friend.",
    "Today",
    "is",
    "a",
    "very",
    "good",
    "day.",
]
sentences = ["Hello, my little friend", "Today is a very good day."]

message_from_words = " ".join(words)
message_from_sentences = ". ".join(sentences)

print(message_from_words)  # Hello, my little friend. Today is a very good day.
print(message_from_sentences)  # Hello, my little friend. Today is a very good day.
'''
## поділ на частини. маркер поділу пробіли  
# text = 'First sentance. Second sentance. Thirdsentance'
# sentances = text.split('.')        
# print(sentances)      # ['First', 'sentance.', 'Second', 'sentance.', 'Thirdsentance']

## поділ на частини. маркер поділу '.' 
# text = 'First sentance. Second sentance. Thirdsentance'
# sentances = text.split('.')        
# print(sentances)        # ['First sentance', ' Second sentance', ' Thirdsentance']

## поділ на частини. маркер поділу '.' 
# text = 'First sentance. Second sentance. Thirdsentance'
# sentances = text.split('.') 
# print(s)        # ['First sentance', ' Second sentance', ' Thirdsentance']

## поділ на частини, якщо речення поділено різними розділовими знаками
# import re
# text = 'First sentance. Second sentance! Thirdsentance?'
# sentances = re.split('[\.\!\?]', text)  
# print(sentances)        # ['First sentance', ' Second sentance', ' Thirdsentance', '']

## якщо текст поділений за допомогою \n 
# text = 'First sentance.\nSecond sentance!\nThirdsentance?'

# print(text)
# sentances = text.split('\n')  
# print(sentances) 
# new_text = ' '.join(sentances)  # join збирає список в строку
# print(new_text)              # First sentance. Second sentance! Thirdsentance? 

'''
Метод translate
Метод translate у Python дозволяє замінити символ у рядку на інший з карти (таблиці) відповідності, котру можна задати. Якщо ми використовуємо словник, ми повинні використовувати ASCII коди замість символів.

Приклад:
replace_dict = {117: "o"}
txt = "sun"
print(txt.translate(replace_dict))  # son
Що сталося? Ми замінили в тексті символ "u" на символ "o". Значення 117 — це ASCII код символу 'u', яке, як знаємо, можна отримати з допомогою функції ord("u").

replace_dict = {ord("u"): "o"}
txt = "sun"
print(txt.translate(replace_dict))  # son
Таким чином translate() – метод, який повертає рядок, де деякі задані символи замінюються на символи, описані у словнику, або таблиці відображення. Якщо символ не вказано у словнику/таблиці, символ не буде замінено. Для створення таблиці відображення використовується метод maketrans.

txt = "sun"
my_table = txt.maketrans("u", "o")
print(txt.translate(my_table))  # son
Можна визначити набір для замін

txt = "sun"
my_table = txt.maketrans("nus", "mot")
print(txt.translate(my_table))  # tom
Третій параметр у таблиці зіставлення описує символи, які ви хочете видалити з рядка:

txt = "the sun"
my_table = txt.maketrans("nus", "nos", "he t")
print(txt.translate(my_table))  # son
Якщо ми збираємося транслювати кирилицю на латиницю, у нас може виникнути проблема, наприклад, при транслітерації 
слова "чаша", яке має бути "chasha" і має довжину на два символи більше. Використання maketrans викличе помилку. Як бути?

Для цього можна використовувати вбудовану функцію zip, яка перетворює численні об'єкти, що ітеруються в єдиний об'єкт                                                                                                                              
кортежів, що ітерується, та складається з відповідних елементів:

CYRILLIC = ("а", "ч", "ш")
LATIN = ("a", "ch", "sh")

TRANSLIT_DICT = {}

for c, l in zip(CYRILLIC, LATIN):
    TRANSLIT_DICT[ord(c)] = l
    TRANSLIT_DICT[ord(c.upper())] = l.upper()

print("чаша".translate(TRANSLIT_DICT))  # chasha
print("ЧАША".translate(TRANSLIT_DICT))  # CHASHA
Так швидко можна створити словник для транслітерації. Якщо списки мають різні довжини, то функція zip припинить роботу, щойно закінчиться перший із них.
'''

# trans_map = {ord('Я'): 'Ya', ord('н'): 'n', ord('а'): 'a'}  
# ukr_name = "Яна"
# last_name = ukr_name.translate(trans_map)
# print(ukr_name, '=', last_name, sep=' ')    # Яна = Yana

## використання для пошуку в строках
# trans_map = {ord('Я'): 'Ya', ord('н'): 'n', ord('а'): 'a', ord('о'): 'o'}  
# text = "Hello Wоrld"                    # o не латинська а українська
# index = text.find('World')
# new_index = text.translate(trans_map).find('World')
# print(index)                            # -1
# print(new_index)                        # 6

'''
Регулярні вирази 
----------
У програмуванні регулярні вирази (від англ. Regular expression, скорочено regex або regexp) — це рядок, який описує деяку множину рядків відповідно до набору спеціальних синтаксичних правил wiki .
Регулярні вирази — це окрема псевдомова програмування, яка широко використовується у багатьох мовах програмування і в Python у тому числі.
Детальне вивчення синтаксису регулярних виразів виходить за рамки цього курсу. Кому цікаво, можете продовжити знайомство з регулярними виразами за посиланням чи детальніший опис з прикладами тут.
Основне завдання регулярних виразів — це пошук рядка, або підрядка, який відповідає опису в термінах регулярних виразів.
Використовуючи цей механізм можна:
- перевіряти, що рядок відповідає деяким вимогам (це номер телефону або email);
- розділяти рядки на підрядки за деяким виразом (розбити текст на пропозиції, використовуючи усі розділові знаки, а не тільки якийсь один);
- замінювати підрядок в рядку (замінити усі слова, що починаються на деяку послідовність);
- знаходити підрядок в рядку, який відповідає виразу;
Регулярний вираз, або коротко "регулярка", складається із звичайних символів і спеціальних командних послідовностей. Наприклад, \d задає будь-яку цифру, а \d+ — задає будь-яку послідовність із однієї або більше цифр.
Гарна стаття на тему регулярних виразів є на хабрі, там багато прикладів і корисних посилань.
У модулі re у Python є набір інструментів для роботи з регулярними виразами у Python. Щоб скористатися цим модулем, його треба спочатку імпортувати:

import re

Модуль пропонує набір функцій, який дозволяє нам шукати рядки на збіг:
Функція	    Опис
findall	    Повертає список, забезпечує всі збіги
search	    Повертає об'єкт Match, якщо у рядку є збіг
split	    Повертає список, де рядок був розділений при кожному збігу
sub	        Замінює один або кілька збігів рядком
Загальним для усіх функцій модуля re є те, що першим аргументом йде регулярний вираз у вигляді рядку.

Пошук на відповідність регулярному виразу виконує функція search модуля re. В результаті її виконання повертається спеціальний об'єкт Match або None, якщо нічого не знайшлося.

s = "I am 25 years old"
age = re.search('\d+', s)
print(age)  # <re.Match object; span=(5, 7), match='25'>
Щоб витягнути власне знайдене значення із age, можна скористатися його методом group

s = "I am 25 years old."
age = re.search('\d+', s)
print(age.group())  # 25
Функція search — "ледача" і знаходить тільки першу відповідність заданій умові.

Об'єкт Match має властивості та методи, що використовуються для отримання інформації про пошук та результат:
- Match.span() повертає кортеж, що містить початкову та кінцеву позиції збігу.
- Match.string повертає рядок, переданий у функцію,
- Match.group() повертає частину рядка, в якому був збіг
------------------
'''
'''
До цього моменту ми використовували функцію findall. Результат виконання відповідає всім входженням шаблону, а не тільки першому, як, наприклад, у функції search.
Але якщо ми бажаємо отримати більше інформації про всі збіги шаблону, ніж список тексту від findall, необхідно використовувати finditer — це корисно, оскільки вона надає об'єкти збігів замість рядків.
re.finditer(pattern, string, flags=0)
Функція finditer повертає ітератор, що дає об'єкти збігів по всіх збігах, що не перекриваються для шаблону pattern у рядку string. Рядок сканується зліва направо, а збіги повертаються в тому порядку, в якому їх знайшли.
Найкраще — це показати на прикладі 13 завдання, знаходження email адрес.
import re
regex = r"[a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-Z]{2,}"
test_str = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"
matches = re.finditer(regex, test_str)
for match in matches:
    print(f"{match.group()} start: {match.start()} end: {match.end()}")
Результат виводу:
Ima.Fool@iana.org start: 0 end: 17
Fool@iana.org start: 35 end: 48
first_last@iana.org start: 49 end: 68
first.middle.last@iana.or start: 69 end: 94
abc111@test.com start: 106 end: 121
'''