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


def decimal_to_hexadecimal(string):
    # ignoring everything but numbers and .
    new_string = [n for n in string if n.isnumeric() or n in ['.']]
    if [n for n in string if n.isnumeric()]:
        number1 = int(''.join(new_string).split('.')[0])
        number2 = '.' + (''.join(new_string).split('.')[1]) if '.' in str(new_string) else ''
        str_num1 = str(hex(number1))
        str_num2 = decimal_dot_to_binary('0.' + (''.join(new_string).split('.')[1]), 16) if '.' in str(
            new_string) else ''
        return ' عشري ' + str(number1) + str(number2) + ' --- > ' + ' سداسي عشر ' + str_num1.replace('0x', '') + str_num2
    else:
        return 'بس هاي الرسالة مابيهة رقم :('


def decimal_dot_to_binary(num, multiplier):  # I used it to all numbers not just binary
    num = float(num)
    limit = 18
    num_list = []
    while num not in range(1, 16) and limit > 0:
        if num > 1:
            num = float('0.' + (str(num).split('.')[1]))
        limit -= 1
        num = num * multiplier   # should make this more efficient
        if 16 > num >= 15:
            num_list.append('F')
        elif 15 > num >= 14:
            num_list.append('E')
        elif 14 > num >= 13:
            num_list.append('D')
        elif 13 > num >= 12:
            num_list.append('C')
        elif 12 > num >= 11:
            num_list.append('B')
        elif 11 > num >= 10:
            num_list.append('A')
        else:
            num_list.append(str(num).split('.')[0])
        # print(num_list)

    if limit <= 0:
        print("error the limit have been reached")
        return '.' + ''.join(num_list) if num_list else ''
    else:
        return '.' + ''.join(num_list)


def to_decimal(stri, formating):
    the_list = ['.', 'a', 'b', 'c', 'd', 'e', 'f']
    number = ''.join([n for n in stri if n.isnumeric() or n in the_list])
    number1 = number.split('.')[0]
    number2 = number.split('.')[1] if '.' in number else ''
    print('number ' + number)
    print('number ' + number1 + '.' + number2)
    answer = []
    answer2 = []
    highest_pow = len(number.split('.')[0]) - 1
    print('highest power ' + str(highest_pow))
    for num in number1:
        if int(num.replace('a','10').replace('b','11').replace('c','12').replace('d','13').replace('e','14').replace('f','15')) > formating:
            return 'هاي وين يصير نحل بهيج ارقام..'

        if num in the_list[1:]:
            answer.append((the_list[1:].index(num)+10) * (formating ** highest_pow))

        else:
            answer.append(int(num) * (formating ** highest_pow))
        highest_pow -= 1
    answer = sum(answer)
    print(f'answer is {answer}')
    for num2 in number2:
        if int(num2.replace('a', '10').replace('b', '11').replace('c', '12').replace('d', '13').replace('e','14').replace('f', '15')) > formating:
            return 'هاي وين يصير نحل بهيج ارقام..'
        if num2 in the_list[1:]:
            answer2.append((the_list[1:].index(num2) + 10) * (formating ** highest_pow))

        else:
            answer2.append(int(num2) * (formating ** highest_pow))
        highest_pow -= 1
    answer2 = sum(answer2)
    print(f'answer2 is {answer2}')
    type = ''
    if formating == 2:
        type = 'ثنائي'
    elif formating == 8:
        type = 'ثماني'
    elif formating == 16:
        type = 'سداسي عشر'


    final_answer = str(answer + answer2)
    return type + ' ' + number + ' ----> ' + 'عشري ' + final_answer


# print(to_decimal('c0a.1f', 16))
