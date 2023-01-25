def day_1_2022(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    f.close()
    lines = list(map(lambda x: x.replace('\n', ''), lines))
    temp_value = []
    sum = 0
    for each in lines:
        if each != '':
            sum += int(each)
        else:
            temp_value.append(sum)
            sum = 0
    result = 0
    for i in range(3):
        result += max(temp_value)
        temp_value.remove(max(temp_value))

    return result


def day_2_2022(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    f.close()
    temp_sum = []
    score = 0
    temp_result = 0
    lines = list(map(lambda x: x.replace('\n', ''), lines))
    # first part of solution
    # for each in lines:
    #     if 'X' in each:
    #         score = 1
    #     elif 'Y' in each:
    #         score = 2
    #     elif 'Z' in each:
    #         score = 3
    #     if ('A' in each and 'Y' in each) or ('B' in each and 'Z' in each) or ('C' in each and 'X' in each):
    #         temp_result = 6
    #     elif ('A' in each and 'X' in each) or ('B' in each and 'Y' in each) or ('C' in each and 'Z' in each):
    #         temp_result = 3
    #     else:
    #         temp_result = 0
    #     temp_sum.append(score+temp_result)

    for each in lines:
        if 'X' in each:
            if 'A' in each:
                score = 3
            elif 'B' in each:
                score = 1
            elif 'C' in each:
                score = 2

            temp_result = 0
        elif 'Y' in each:
            if 'A' in each:
                score = 1
            elif 'B' in each:
                score = 2
            elif 'C' in each:
                score = 3

            temp_result = 3
        elif 'Z' in each:
            if 'A' in each:
                score = 2
            elif 'B' in each:
                score = 3
            elif 'C' in each:
                score = 1

            temp_result = 6
        temp_sum.append(score+temp_result)
    return sum(temp_sum)


def day_3_2022(file_name):
    with open(file_name) as f:
        read_lines = f.readlines()
    f.close()
    read_lines = [each.replace('\n', '') for each in read_lines]
    length = 0
    first_part = []
    temp_result, second_part = [], []
    # first part of chalange:
    for each in read_lines:
        length = int(len(each)/2)
        first_part = each[:length]
        second_part = each[length:]
        fist_char = list(map(lambda x: ord(x), first_part))
        second_char = list(map(lambda x: ord(x), second_part))
        for i in fist_char:
            if i in second_char:
                if i > 96:
                    temp_result.append(i-96)
                else:
                    temp_result.append(i-64+26)
                break

    # second part of chalange:
    first_string, second_string, third_string = '', '', ''
    min_length = 0
    result = []
    for i in range(0, len(read_lines), 3):
        first_string = read_lines[i]
        second_string = read_lines[i+1]
        third_string = read_lines[i+2]
        min_length = sorted(
            [first_string, second_string, third_string], key=len)[0]

        for i in min_length:
            if (i in second_string) and (i in first_string) and (i in third_string):
                if ord(i) > 96:
                    result.append(ord(i)-96)
                else:
                    result.append(ord(i)-64+26)
                break

    return sum(result)


def day_4_2022(file_name):
    with open(file_name) as f:
        readline = [each.replace('\n', '').replace(',', '-')
                    for each in f.readlines()]
    f.close()
    pairs = [each.split('-') for each in readline]
    len_pairs = len(pairs)
    sum = 0

    for each in pairs:
        # first part of solution
        if (int(each[0]) >= int(each[2]) and int(each[1]) <= int(each[3])) or (int(each[0]) <= int(each[2]) and int(each[1]) >= int(each[3])):
            sum += 1
        # second part of solution
        if int(each[0]) > int(each[3]) or int(each[1]) < int(each[2]):
            len_pairs -= 1

    return len_pairs


def day_5_2022(file_name):
    with open(file_name) as f:
        read_lines = [each.replace('\n', '') for each in f.readlines()]
    f.close()
    temp_list = ['']*9
    temp_list_1 = ['']*9
    stock_list = []
    final_list = ''
    moves_list = [each.replace('move ', '').replace('from ', '').replace(
        'to ', '').split(' ') for each in read_lines[10:]]
    for i in range(9):
        temp_list[i] = list(read_lines[i][1::4])
    for i in range(9):
        temp_list_1 = ['']*8
        for j in range(8):
            temp_list_1[j] = temp_list[0:8][j][i].replace(' ', '')

        temp_list_1 = list(filter(None, temp_list_1))
        stock_list.append(temp_list_1[::-1])
        # stock_list = list(filter('', stock_list))

    # for each in moves_list:
    #     number_of_moves = each[0]
    #     stack_from = each[1]
    #     stack_to = each[2]
    #     for i in range(int(number_of_moves)):
    #         stock_list[int(stack_to) -
    #                    1].append(stock_list[int(stack_from) - 1][-1])
    #         stock_list[int(stack_from) - 1].pop()
    # second part of challenge.

    for each in moves_list:
        number_of_moves = each[0]
        stack_from = each[1]
        stack_to = each[2]
        temp_list = stock_list[int(stack_from) - 1][-int(number_of_moves):]
        for each in temp_list:
            stock_list[int(stack_to) - 1].append(each)

        # leave only elements to indicated position
        # remove everything after this index.

        stock_list[int(stack_from) - 1] = stock_list[int(stack_from) -
                                                     1][:len(stock_list[int(stack_from) - 1])-int(number_of_moves)]

    for i in range(9):
        final_list = final_list+stock_list[i][-1]
    return final_list


def day_6_2022(file_name):
    with open(file_name) as f:
        read_lines = [each.replace('\n', '') for each in f.readlines()]
    f.close()
    # internal variable:
    counter = 0
    numebr_of_signs_to_chcek = 14
    list_of_characters = []
    # initialise list of letters
    signs = list(filter(lambda i: (i in read_lines[0]), read_lines[0]))
    # solution for first part of challenge. It needs to be rebuild to fullfill expectation of second part
    # for i in range(len(signs) - 4):

    #     if (signs[i] != signs[i+1]) and (signs[i] != signs[i+2]) and (signs[i] != signs[i+3]) and (signs[i+1] != signs[i+2]) and (signs[i+1] != signs[i+3]) and (signs[i+2] != signs[i+3]):
    #         break
    #     counter += 1

    # Solution for second part of challenge is upgraded version of first part of solution. Changes are quite siginficant:
    # Added dynamic selection of list to verification
    # Modified method of searching characters in selected list
    # Add condition to check how many signs was checked, which indicates if proper sequence was found.
    for i in range(len(signs) - numebr_of_signs_to_chcek):
        list_of_characters = signs[counter:counter+numebr_of_signs_to_chcek]
        checked_signs = 0
        for each in list_of_characters:
            if list_of_characters.count(each) > 1:
                break
            else:
                checked_signs += 1
        if checked_signs == numebr_of_signs_to_chcek:
            break
        counter += 1

    return counter+numebr_of_signs_to_chcek


if __name__ == "__main__":
    # file_name = "C:\\Users\\PiotrKoluda\Desktop\\Calendar of code\\Day10Advent calendar.txt"
    file_name = "C:\\Users\\PiotrKoluda\Desktop\\Calendar of code\\Temp.txt"
    print('result is: {0}'.format(day_6_2022(file_name)))
