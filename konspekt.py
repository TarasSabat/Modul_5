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
## Виключити з цього символів, дужками.
## 1 ітерація циклу-> Виключити з цього  символів, [розташовані між] дужками [, ].
## 2 ітерація циклу-> Виключити з цього  символів,  дужками [, ].
## 3 ітерація циклу-> Виключити з цього  символів,  дужками .

# start_index = string.find('[')
# end_index = string.find(']')
#
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
------
Провести валідацію списку телефонів
Телефон: +380501234567 Де: +380 код країни телефон 501234567
Вважаємо, що код валідний з кодом і без коду
"""
phone_storage = ["380669640547", "0637306465 ", " 380961935171", "632643973", "050832520 ",
                 "000000000", "48730283918", "986223575", "375297947963", "+38(050)123-32-34", "38(050)123 32 34",
                 "38(050)123 32 3b"]

codes_operators = {"067", "068", "096", "097", "098",
                   "050", "066", "095", "099", "063", "073", "093"}

from for_import import sanitize_phone, is_valid_phone

if __name__ == "__main__":
    print('|{:^14}|{:^12}|'.format('Телефон', 'Результат'))
    print('|{:^14}|{:^12}|'.format('-' * 13 + ':', ':' + '-' * 10 + ':'))
    for phone in phone_storage:
        phone = sanitize_phone(phone)
        if is_valid_phone(phone):
            print('|{:>14}|{:^12}|'.format(phone, 'valid'))
        else:
            print('|{:>14}|{:^12}|'.format(phone, 'not valid'))


"""
Є 2 списка телефонів: перший - список усіх реєстрацій, другий - тих, хто підключився до гри.
Визначити список телефонів тих, хто зареєструвався, але не розпочав роботу на сайті.
["380669640547", "0637306465", "380961935171", "632643973", "508325200", "000000000", "48730283918", "986223575", "375297947963"]
["380669640547", "0637306465" "632643973", "508325200", "48730283918", "986223575"]
"""

# ​registration = ["380669640547", "0637306465", "380961935171", "632643973", "508325200", "000000000", "48730283918", "986223575", "375297947963"]
# connect = ["380669640547", "0637306465" "632643973", "508325200", "48730283918", "986223575"]