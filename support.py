# convert decimal numbers to binary
def decimal_to_binary(string):
    # ignoring everything but numbers and .
    new_string = [n for n in string if n.isnumeric() or n in ['.']]
    if [n for n in string if n.isnumeric()]:
        number1 = int(''.join(new_string).split('.')[0])
        number2 = '.' + (''.join(new_string).split('.')[1]) if '.' in str(new_string) else ''
        str_num1 = str(bin(number1))
        str_num2 = decimal_dot_to_binary('0.' + (''.join(new_string).split('.')[1]), 2) if '.' in str(
            new_string) else ''
        return ' عشري ' + str(number1) + str(number2) + ' --- > ' + ' ثنائي ' + str_num1.replace('0b', '') + str_num2
    else:
        return 'بس هاي الرسالة مابيهة رقم :('


def decimal_to_octal(string):
    # ignoring everything but numbers and .
    new_string = [n for n in string if n.isnumeric() or n in ['.']]
    if [n for n in string if n.isnumeric()]:
        number1 = int(''.join(new_string).split('.')[0])
        number2 = '.' + (''.join(new_string).split('.')[1]) if '.' in str(new_string) else ''
        str_num1 = str(oct(number1))
        str_num2 = decimal_dot_to_binary('0.' + (''.join(new_string).split('.')[1]), 8) if '.' in str(
            new_string) else ''
        return ' عشري ' + str(number1) + str(number2) + ' --- > ' + ' ثماني ' + str_num1.replace('0o', '') + str_num2
    else:
        return 'بس هاي الرسالة مابيهة رقم :('


def decimal_dot_to_binary(num, multiplier):
    num = float(num)
    limit = 18
    num_list = []
    while num not in range(1, 7) and limit > 0:
        if num > 1:
            num = float('0.' + (str(num).split('.')[1]))
        limit -= 1
        num = num * multiplier
        num_list.append(str(num).split('.')[0])
        print(num_list)

    if limit <= 0:
        print("error the limit have been reached")
        return '.' + ''.join(num_list) if num_list else ''
    else:
        return '.' + ''.join(num_list)


# print(decimal_to_octal('hewllo baby  73.25'))
