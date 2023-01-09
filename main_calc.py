CONDITION = '''Выберите операцию:
Сложить: +
Вычесть: -
Умножить: *
Разделить: /''' # Варианты операций
GOODBYE = 'До свидания!' # Прощаемся при выходе
INSTRUCTION = '''Данный калькулятор является простым в использовании:
1. Вводим первое число
2. Выбираем операцию
3. Вводим второе число
---
Чтобы выйти из калькулятора в любом месте, введите "Q".
---
Если вы ошиблись при наборе цифры или операции, не беда - калькулятор снова предложит вам ввести значение.
---
Для того, чтобы снова ввести число, введите 'U' (от англ. update - обновлять)
'''

def quit_programm(Q):
    if f_num == 'Q' or s_num == 'Q' or oper == 'Q':
        print('До свидания!')
        quit()

f_num = None
s_num = None
oper = None

print(INSTRUCTION)
while True:
    f_num = input('Введите первое число: ')
    quit_programm(f_num)
    while f_num.isdigit() == False:
        print('Вы ввели неверное значение')
        f_num = input('Введите Q для выхода или введите первое число: ')
        quit_programm(f_num)
    print(CONDITION)
    oper = input()
    quit_programm(oper)
    while oper not in('+', '-', '*', '/', 'Q'):
        print(CONDITION)
        oper = input()
        quit_programm(oper)
    s_num = input('Введите второе число: ')
    quit_programm(s_num)
    while s_num.isdigit() == False:
        print('Вы ввели неверное значение')
        s_num = input('Введите Q для выхода или введите второе число: ')
        quit_programm(s_num)
    if oper == '+':
        print(int(f_num) + int(s_num))
    elif oper == '-':
        print(int(f_num) - int(s_num))
    elif oper == '*':
        print(int(f_num) * int(s_num))
    elif oper == '/':
        try:
            print(int(f_num) / int(s_num))
        except ZeroDivisionError:
            print('Делить на 0 нельзя!')
    y = input('''Если хотите продолжить, введите "y" или "да"
    Если хотите выйти, введите "no" или "нет"
               ''')
    if y == 'y' or y == 'да':
        continue
    elif y == 'no' or y == 'нет':
        break
    else:
        print(INSTRUCTION)
