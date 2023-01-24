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


if __name__ == "__main__":
    # file_name = "C:\\Users\\PiotrKoluda\Desktop\\Calendar of code\\Day10Advent calendar.txt"
    file_name = "C:\\Users\\PiotrKoluda\Desktop\\Calendar of code\\Temp.txt"
    print('result is: {0}'.format(day_4_2022(file_name)))
