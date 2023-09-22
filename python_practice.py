# -*- coding: utf-8 -*-
"""python_practice_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KJVrf5F0Y49FmGP9gFBxlvMOp5znF_bk

# I. Змінні та памʼять.

1. Створити змінні, що посилаються на два цілих числа, що однакові за значенням, де значення належить проміжку від -5 до 256. Чи будуть ці змінні рівні тільки за значенням або ж ще будуть посилатися на один і той самий обʼєкт в памʼяті? Наведіть код та дайте текстову відповідь нижче.
"""

new_int=255
new_int2=255

print(new_int,new_int2)
print(id(new_int),id(new_int2))

"""2. Створити змінні, що посилаються на одне і те саме булеве значення. Чи будуть ці змінні рівні тільки за значенням або ж ще будуть посилатися на один і той самий обʼєкт в памʼяті? Наведіть код та дайте текстову відповідь нижче."""

new_boolean = True
new_boolean2 = True

print(id(new_boolean),id(new_boolean2))

"""*місце для текстової відповіді або коментарів *текст курсивом*

*Як ми бачимо, якщо числа однакові за значенням, то для них виділяється одна комірка пам'яті.*

*Булеве значення займають одну й ту саму комірку пам'яті.*

3. За допомогою якої функції можна перевірити належність змінної до вказаного типу даних (напр. чи змінна посилається на значення булевого типу)?
"""

type(new_boolean2), type(new_int)

"""# II. Цілі числа та числа з рухомою комою

4. Створити дві змінні, що посилаються на будь-які два цілих числа та продемонструвати такі арифметичні операції: додавання, віднімання, ділення, множення, ділення без залишку, ділення по модулю, приведення до ступеню. Всі результати операцій вивести на екран.
"""

int_a = 15
int_b = 4

print(int_a + int_b, int_a - int_b, int_a/int_b, int_a*int_b)
print(int_a//int_b, int_a%int_b, int_a**int_b)

"""5. Створити дві змінні, що посилаються на будь-які два числа з рухомою комою та продемонструвати такі арифметичні операції: додавання, віднімання, ділення, множення, ділення без залишку, ділення по модулю, приведення до ступеню. Всі результати операцій вивести на екран."""

float_a = 3.3
float_b = 1.9

print(float_a + float_b, float_a - float_b, float_a/float_b, float_a*float_b)
print(float_a//float_b, float_a%float_b, float_a**float_b)

"""6. Спробуйте проробити всі ті самі арифметичні операції над двома змінними, що посилаються на різні булеві значення. Прокоментуйте, чому, на Вашу думку, Ви отримали саме такі результати."""

boolean_a = True
boolean_b = False

print(boolean_a + boolean_b, boolean_a - boolean_b, boolean_b/boolean_a, boolean_a*boolean_b)
print(boolean_b//boolean_a, boolean_b%boolean_a, boolean_a**boolean_b)

"""*місце для текстової відповіді або коментарів*

*Бо True відповідає значенню 1, а False відповідає значенню 0.*

7. Використовуючи змінні з вправи 3, продемонструйте механізм явного перетворення типів, де числа з рухомою комою перетворюються на цілі числа.
"""

print(int(float_a),int(float_b))

"""# III. Робота зі списками.

8. Створити список двома різними за синтаксисом способами. За допомогою вбудованої функції обчисліть довжину одного з них.
"""

new_list = [1,2,3]
new_list2 = list((4,5,6))

print(len(new_list2))

"""9. Створіть два списка та за допомогою спеціального методу додайте другий з них в якості останнього елемента першого."""

normal_list = [1,2,3]
normal_list2 = [4,5,6]

normal_list2.append(normal_list)
print(normal_list2)

"""10. Створіть два списка та за допомогою спеціального методу "розширте" перший (додайте всі елементи другого в кінець першого списку). Напишіть, чим відрізняються методи в завданні 9 та 10."""

special_list = [1,2,3]
special_list2 = [4,5,6]

special_list2.extend(special_list)
print(special_list2)

"""*місце для відповіді*

*Метод append додає список як цілий елемент, а метод extend розширює список усіма елементами другого списка.*

11. Створіть список та відсортуйте його так, щоб:
а) його id залишився незмінним після сортування.
б) результат сортування був збережений у нову змінну. Підказка: для одного пункту використовуйте вбудовану функцію стортування, а в іншому - спеціальний метод для роботи зі списками.
"""

# a
unsorted_list =[2,5,89,1,9,1,0,45,10]
print(sorted(unsorted_list))

# b
unsorted_list2 =[2,5,89,1,9,1,0,45,10]
sorted_list = sorted(unsorted_list2)
print(sorted_list)

"""12. Створіть список з елементами різного типу, де деякі значення елементів повторюються. За допомогою спеціального методу порахуйте кількість значень одного з елементів на Ваш вибір. Результат виведіть на екран."""

my_list = [1, 'apple', 2.5, 'banana', 1, 'cherry', 1, True, 2.5]
count_1_in_list = my_list.count(1)
print(count_1_in_list)

"""# IV. Робота з кортежами.

13. Створити список з один типом елементів та на основі цього списку створити кортеж.
"""

integer_list = [1,5,6,3,6]
my_int = tuple(integer_list)
print(my_int)

"""14. Створити кортеж з один елементом."""

new_tuple = (1,)
print(new_tuple)

"""15. Створити кортеж. Вивести на екран всі доступні його атрибути та методи."""

my_tuple = (1,5,43,7,"Tom")
print(dir(my_tuple))

"""16. Порівняйте список та кортеж. Назвіть схожості та відмінності, випадки використання.

**місце для відповіді*
*Відмінність між Tuple та List це декларація, швидкість та те що Tuple не можна змінювати.*
*Схожості між Tuple та List це індексація елементів та ітерація.*
*Застосування Tuple: для зберігання або передачу даних, які не поавинні змінюватися.*
*Застосування List: для зберігання даних, які можно змінювати та для зберігання послідовностей елементів.*

# V. Індексування та слайсинг.

17. Створіть список з 6ти елементів. Отримайте третій елемент за допомогою двох різних індексів.
"""

my_list3 = [1,3,4,7,2,8]
print(my_list3[2],my_list3[-4])

"""18. Створіть список, де елементами цього списку також є списки. Отримай перший елемент з останнього рядка та виведи значення на екран."""

listed_list = [[1,2,3],[4,5,6],[7,8,9]]
last_row = listed_list[-1]
first_element_of_last_row = last_row[0]

print(first_element_of_last_row)

"""19. Створіть кортеж, що містить 8  елементів цілочисленного типу. Виведіть на екран три найменших значення."""

integer_tuple = [5,6,3,78,187,1,9,1]
sorted_tuple = sorted(integer_tuple)
print(sorted_tuple[:3])

"""20. Створіть список з десяти елементів різного типу. Отримайте всі елементи, окрім двох перших та двох останніх та збережіть їх в новій змінній."""

my_list2 = [1, 'hello', 3.14, [4, 5], True, 'world', 7, (8, 9), False, 10]
new_list3 = my_list2[2:-2]
print(new_list3)

"""21. Створіть кортеж з 11ти елементів чисел з рухомою комою та отримайте кожен парний за індексом елемент в зворотньому порядку. Наприклад, маючи (1.2, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3, 8.3, 9.3, 0.3), отримати (0.3, 8.3, 6.3, 4.3, 2.3). Результат збережіть в нову змінну та виведіть на екран."""

float_tuple = (1.2, 2.3, 3.3, 4.3, 5.3, 6.3, 7.3, 8.3, 9.3, 0.3, 11.2)
result_tuple = float_tuple[-2::-2]

print(result_tuple)

"""# Вітаю! Ви велика(ий) молодець, що впоралась(вся). Похваліть себе та побалуйте чимось приємним. Я Вами пишаюся."""