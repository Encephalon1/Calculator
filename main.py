def calculator():
    mathem = input('Введите математическое выражение через пробел (например, 2 + 2): ')
    mathem_list = list(mathem.split(' '))
    
    # Для правильного порядка действий
    result = 0
    num2 = 0
    num3 = 0
    operation1 = '+'
    operation2 = '+'
    num = 0

    for i in mathem_list:
        # Сначала переводим строку в число, заодно отлавливаем ошибку
        if i != '+' and i != '-' and i != '*' and i != '/':
            try:
                i = int(i)
            except ValueError:
                print('Некорректное выражение!')
                return

        # Здесь сдвигаемся по выражению слева направо, по одному символу
        if type(i) == int:
            if result == 0:
                result = i
            else:
                num2 = num3
                num3 = i
        else:
            operation1 = operation2
            operation2 = i

        if i != '+' and i != '-' and i != '*' and i != '/': # Чтобы не выполнялись лишние действия
            # Правильный порядок действий
            if operation2 == '*' and operation1 != '*' and operation1 != '/':
                num = num2 * num3
                if operation1 == '+':
                    result += num
                elif operation1 == '-':
                    result -= num
            elif operation2 == '/' and operation1 != '*' and operation1 != '/':
                num = num2 / num3
                if operation1 == '+':
                    result += num
                elif operation1 == '-':
                    result -= num
            else:
                if operation1 == '+':
                    result += num2
                elif operation1 == '-':
                    result -= num2
                elif operation1 == '*':
                    result *= num2
                elif operation1 == '/':
                    result = result / num2

    print(result)


calculator()
