'''
Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]
Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:
'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'
'''

# def real_len(text):
#     chars = '\n, \f, \r, \t, \v'
#     text_1 = text.translate(str.maketrans('','', chars))
#     text_len = len(text_1)
#     return text_len

# print(real_len('Alex\nKdfe23\t\f\v.\r'))
'''
Ваша компанія веде блог. Треба реалізувати функцію find_articles для пошуку за статтями цього блогу. Є список articles_dict, в якому міститься опис статей блогу. Кожен елемент цього списку є словником з наступними ключами: прізвища авторів - ключ 'author', назва статті - ключ 'title', рік видання - ключ 'year'.
Реалізуйте функцію find_articles,
Параметр key функції визначає поєднання букв для пошуку. Наприклад, при key="Python" функція шукає, чи є у списку articles_dict статті, у назві чи іменах авторів яких зустрічається це поєднання літер. Якщо такі елементи списку були знайдені, треба повернути новий список зі словників, що містять прізвища авторів, назву та рік видання всіх таких статей.
Другий ключовий параметр функції letter_case визначає, чи треба враховувати під час пошуку регістр літер. За умовчанням він дорівнює False і регістр немає значення тобто пошук в тексті "Python" і "python" це те ж саме. Інакше потрібно шукати повний збіг.
'''
# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]

# def find_articles(key, letter_case=False):
#      articles = []
#      if letter_case:
#          for article in articles_dict:
#              for keys, value in article.items():
#                  if key in str(value):
#                          articles.append(article)
#      else:
#          for article in articles_dict:
#              for keys, value in article.items():
#                  if key.lower() in str(value).lower():
#                          articles.append(article)
#      return articles   

# print(find_articles('Endless'))

'''
Ваша компанія проводить маркетингові кампанії за допомогою SMS-розсилок. Автоматичний збір телефонних номерів із бази даних формує певний перелік. Але клієнти залишають свої номери у довільному вигляді:
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
Сервіс розсилок чудово розуміє і може відправити SMS клієнту, тільки якщо телефонний номер містить правильні цифри. Необхідно реалізувати функцію sanitize_phone_number, яка прийматиме рядок з телефонним номером та буде нормалізувати його, тобто. буде прибирати символи (, -, ), + та пробіли.
Результат:
380501233234
0503451234
0508889900
380501112222
380501112211
'''
# def sanitize_phone_number(phone):
#     chars = '(', '-', ')', '+', ' ' 
#     phone_norm = phone.translate(str.maketrans('','', str(chars)))
#     return phone_norm

# print(sanitize_phone_number("     0503451234"))

'''
У модулі роботи з функціями ми писали функцію get_fullname для складання повного імені користувача. Виконаємо невелике продовження для цього завдання та напишемо функцію is_check_name, яка приймає два параметри (fullname, first_name) і повертає логічне значення True або False. Це результат перевірки, чи є рядок first_name префіксом рядка fullname. Функція is_check_name чутлива до регістру літер, тобто "Sam" і "sam" для неї різні імена.
'''
# def is_check_name(fullname, first_name):
#     fullname_low = fullname.lower()
#     first_name_low = first_name.lower()
#     if fullname_low.startswith(first_name_low, 0, -1):
#         return True
#     else:
#         return False

# print(is_check_name('Max Old', 'Alex'))
'''
Повернемося до нашого завдання із телефонними номерами. Компанія розширюється та вийшла на ринок Азії. Тепер у списку можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код .
Компанія працює з наступними країнами
Країна	Код ISO	Префікс
Japan	JP	+81
Singapore	SG	+65
Taiwan	TW	+886
Ukraine	UA	+380
Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно створити для кожної країни свій список телефонних номерів.
Напишіть функцію get_phone_numbers_for_сountries, яка буде:
Приймати список телефонних номерів.
Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
Сортувати телефонні номери за вказаними у таблиці країнами.
Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
{
    "UA": [<тут список телефонів>],
    "JP": [<тут список телефонів>],
    "TW": [<тут список телефонів>],
    "SG": [<тут список телефонів>]
}
Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.
'''
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone

# def get_phone_numbers_for_countries(list_phones):
#     phone_numbers_for_countries = {"UA": [], "JP": [], "TW": [], "SG": []}
    
#     if len(list_phones) == 0:
#         return phone_numbers_for_countries
    
#     for el in list_phones:
#         tel = sanitize_phone_number(el)
#         if tel.startswith("81"):
#             phone_numbers_for_countries.get("JP").append(tel)
#             continue
#         elif tel.startswith("886"):
#             phone_numbers_for_countries.get("TW").append(tel)
#             continue
#         elif tel.startswith("65"):
#             phone_numbers_for_countries.get("SG").append(tel)
#             continue
#         else:
#             phone_numbers_for_countries.get("UA").append(tel)
#     return phone_numbers_for_countries

# print(get_phone_numbers_for_countries(['380998759405', '818765347', '8867658976', '657658976']))

'''
Розглянемо завдання на перевірку спаму в електронному листі або фільтрацію заборонених слів у повідомленні.
Нехай функція is_spam_words приймає рядок (параметр text), перевіряє його на вміст заборонених слів зі списку (параметр spam_words), і повертає результат перевірки: True, якщо є хоч одне слово присутнє зі списку, та False, якщо в тексті стоп-слів не виявлено.
Слова у параметрі text можуть бути у довільному регістрі, а значить функція is_spam_words, при пошуку заборонених слів, регістру незалежна і весь текст має зводитися до нижнього регістру. Для спрощення, будемо вважати, що в рядку є тільки одне заборонене слово.
Передбачити третій параметр функції space_around, який за замовчуванням дорівнює False. Він відповідатиме за те, що функція шукатиме окреме слово чи ні. Слово вважати, що стоїть окремо, якщо ліворуч від слова знаходиться символ пробілу або воно розташоване на початку тексту, а праворуч від слова знаходиться пробіл або символ крапки.
Наприклад, у тексті ми шукаємо слово "лох". То в слові "Молох" виклик та результат буде наступним:
print(is_spam_words("Молох", ["лох"]))  # True
print(is_spam_words("Молох", ["лох"], True))  # False
Тобто у другому випадку слово не окреме і є частиною іншого.
У цьому прикладі функція поверне True в обох випадках.
print(is_spam_words("Ты лох.", ["лох"]))  # True
print(is_spam_words("Ты лох.", ["лох"], True))  # True
'''        
def is_spam_words(text, spam_words, space_around=False):
    text = text.lower().replace(",", "").replace(".", "")
    arr_text = text.split(" ")
    for word in arr_text:
        if space_around:
            for spam in spam_words:
                if spam.lower() == word:
                    return True
        else:
            for spam in spam_words:
                if spam.lower() in word:
                    return True
    return False   

