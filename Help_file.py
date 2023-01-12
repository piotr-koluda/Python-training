
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as sp
import time
import array
from math import copysign


def day_1(file_name):
    depth = []

    counter = 1
    sum1 = 0
    sum2 = 0
    counter2 = 1

    with open(file_name) as f:
        depth = f.readlines()
    f.close()

    for i in range(len(depth)):
        if i > 0:
            if depth[i-1].strip() < depth[i].strip():
                # print("Pomiar i: {0} wartosć pomiaru {1} wartosć pomiaru d2 {2}".format(
                #   i, depth[i-1].strip(), depth[i].strip()))
                counter += 1
        if i > 3:
            sum1 = int(depth[i-3]) + \
                int(depth[i-2]) + int(depth[i-1])
            sum2 = int(depth[i])+int(depth[i-1])+int(depth[i-2])
            if sum1 < sum2:
                counter2 += 1

    return counter, counter2


def day_2(file_name_2):
    lines = []
    horizontal_pos = 0
    depth_aim = 0
    depth = 0

    with open(file_name_2) as f:
        lines = f.readlines()
    f.close()

    # for i in range(len(lines)):
    #     if "forward" in lines[i]:
    #         horizontal_pos += int(lines[i].replace("forward", ""))
    #     if "down" in lines[i]:
    #         depth += int(lines[i].replace("down", ""))
    #     elif "up" in lines[i]:
    #         depth -= int(lines[i].replace("up", ""))
    for i in range(len(lines)):
        if "forward" in lines[i]:
            horizontal_pos += int(lines[i].replace("forward", ""))
            depth += depth_aim*int(lines[i].replace("forward", ""))
        elif "down" in lines[i]:
            depth_aim += int(lines[i].replace("down", ""))
        elif "up" in lines[i]:
            depth_aim -= int(lines[i].replace("up", ""))

    return horizontal_pos*depth


def day_3(file_name_3):
    # no dimentional lists
    report = []

    # open file and ger list of data to check
    with open(file_name_3) as f:
        report = f.readlines()
    f.close()
    # calculate half of list initial

    # report = ['00100', '11110', '10110', '10111', '10101', '01111',
    #           '00111', '11100', '10000', '11001', '00010', '01010']
    # get initial size od string
    # integers
    init_size_list = len(report[0])
    counter = 0

    # dimentional lists

    bit_table = [0] * init_size_list
    gamma = [0]*init_size_list
    epsilon = [0]*init_size_list
    oxygen = [0]*init_size_list
    co2 = [0]*init_size_list
    ox_list = report
    co2_list = report

    while len(ox_list) > 1:
        half_of_list = len(ox_list)/2
        ox_zeros_list = [x for x in ox_list if x[counter] == '0']
        ox_ones_list = [x for x in ox_list if x[counter] == '1']
        if len(ox_zeros_list) > len(ox_ones_list):
            oxygen[counter] = '0'
            ox_list = ox_zeros_list
        elif len(ox_zeros_list) <= len(ox_ones_list):
            oxygen[counter] = '1'
            ox_list = ox_ones_list
        counter += 1

    counter = 0

    while len(co2_list) > 1:
        half_of_list = len(co2_list)/2
        co2_zeros_list = [x for x in co2_list if x[counter] == '0']
        co2_ones_list = [x for x in co2_list if x[counter] == '1']
        if len(co2_zeros_list) <= len(co2_ones_list):
            co2[counter] = '0'
            co2_list = co2_zeros_list
        elif len(co2_zeros_list) > len(co2_ones_list):
            co2[counter] = '1'
            co2_list = co2_ones_list
        counter += 1

    half_of_list = len(report)/2

    co2_int = int(''.join(map(str, co2_list)), 2)
    ox_int = int(''.join(map(str, ox_list)), 2)

    # count first zeros on first position

    # for i in report:
    #     bit_table[0] += int(i[0])
    #     bit_table[1] += int(i[1])
    #     bit_table[2] += int(i[2])
    #     bit_table[3] += int(i[3])
    #     bit_table[4] += int(i[4])
    #     bit_table[5] += int(i[5])
    #     bit_table[6] += int(i[6])
    #     bit_table[7] += int(i[7])
    #     bit_table[8] += int(i[8])
    #     bit_table[9] += int(i[9])
    #     bit_table[10] += int(i[10])
    #     bit_table[11] += int(i[11])

    # for i in range(len(bit_table)):
    #     if bit_table[i] > half_of_list:
    #         gamma[i] = 1
    #         epsilon[i] = 0
    #     else:
    #         bit_table[i] = 0
    #         epsilon[i] = 1

    # gamma_1 = int(''.join(map(str, gamma)), 2)
    # epsilon_1 = int(''.join(map(str, epsilon)), 2)

    return co2_int*ox_int


def day_4(file_name):

    bingo = []
    boards = []
    board = []
    temp = ""
    counter = 0
    with open(file_name) as f:
        8
        bingo = f.readlines()
    f.close
    # temp bingo result
    First_row = bingo[0]
    for i in bingo:
        if i != First_row and i != '\n':
            i = i.replace("  ", " ").strip()
            board.append(i.replace('\n', '').split(' '))

        elif i == '\n':
            boards.append(board)
            board = []
    boards.append(board)
    boards = list(filter(None, boards))

    wining_board = []
    break_loops = False
    leave = False

    sum_column = 0

    for i in list(First_row.replace('\n', '').split(",")):
        for j in range(len(boards)):
            if boards[j] != None:
                # if break_loops:
                #     break
                if i in boards[j][0]:
                    temp = [j for j, x in enumerate(boards[j][0]) if x == i]
                    boards[j][0][temp[0]] = "-1"
                if i in boards[j][1]:
                    temp = [j for j, x in enumerate(boards[j][1]) if x == i]
                    boards[j][1][temp[0]] = "-1"
                if i in boards[j][2]:
                    temp = [j for j, x in enumerate(boards[j][2]) if x == i]
                    boards[j][2][temp[0]] = "-1"
                if i in boards[j][3]:
                    temp = [j for j, x in enumerate(boards[j][3]) if x == i]
                    boards[j][3][temp[0]] = "-1"
                if i in boards[j][4]:
                    temp = [j for j, x in enumerate(boards[j][4]) if x == i]
                    boards[j][4][temp[0]] = "-1"
                # boards[j] = list(filter(None, boards[j]))

                for l in range(5):
                    sum_column = 0
                    for k in range(5):
                        if boards[j][k][l] == "-1":
                            sum_column = sum_column+1

                    if boards[j][l].count('-1') == 5 or sum_column == 5:
                        if len(boards) != 1:
                            boards[j] = None
                            break
                        else:
                            break_loops = True
                            break

        if None in boards:
            # wining_board = boards[j]
            boards = list(filter(None, boards))
            # leave = True

        if break_loops:
            boards = list(filter(None, boards))
            wining_board = boards[0]
            break
    for l in range(len(wining_board)):
        wining_board[l] = list(filter(lambda a: a != '-1', wining_board[l]))
    wining_board = list(filter(None, wining_board))

    temp_sum = sum(sum(int(x)
                   for x in wining_board[l]) for l in range(len(wining_board)))

    return temp_sum * int(i)


def day_5(file_name):
    len_coordiantes = 0

    with open(file_name) as f:
        list_of_coordinates = f.readlines()
    f.close

    len_coordiantes = len(list_of_coordinates)

    clear_list = ['']*len_coordiantes
    x_list = [[]]*len_coordiantes
    y_list = [[]]*len_coordiantes
    diagonal = [[]]*len_coordiantes  # part 2

    for i in range(len(list_of_coordinates)):
        clear_list[i] = list_of_coordinates[i].strip().replace(' -> ', ',')
        if clear_list[i].split(",")[0] == clear_list[i].split(",")[2]:
            x_list[i] = clear_list[i].split(",")
        elif clear_list[i].split(",")[1] == clear_list[i].split(",")[3]:
            y_list[i] = clear_list[i].split(",")
        # part 2
        elif (int(clear_list[i].split(",")[1])-int(clear_list[i].split(",")[3]))**2 == (int(clear_list[i].split(",")[0])-int(clear_list[i].split(",")[2]))**2:
            diagonal[i] = clear_list[i].split(",")

    x_list = list(filter(None, x_list))
    y_list = list(filter(None, y_list))
    diagonal = list(filter(None, diagonal))  # part 2
    x_list.sort()
    max_y_int = 0

    max_y_int = int(max(max(max(x_list, key=lambda y: y[1])), max(
        max(y_list, key=lambda y: y[1]))))

    combined_list = x_list + y_list + diagonal

    valve_list = [[]]*(max_y_int+1)
    for i in range(len(valve_list)):
        valve_list[i] = [0]*len(valve_list)

    for each in combined_list:
        if each[0] == each[2]:
            for i in range(min(int(each[1]), int(each[3])), max(int(each[1]), int(each[3]))+1):

                valve_list[i][int(each[0])] = int(
                    valve_list[i][int(each[0])])+1

        elif each[1] == each[3]:
            for i in range(min(int(each[0]), int(each[2])), max(int(each[0]), int(each[2]))+1):
                valve_list[int(each[1])][i] = int(
                    valve_list[int(each[1])][i]) + int(1)
        # part 2 below
        elif (int(each[0])-int(each[2]))**2 == (int(each[1])-int(each[3]))**2:

            max_diag_1 = 0
            max_daig_2 = 0
            distance_x = abs(int(each[2]) - int(each[0]))
            distance_y = abs(int(each[3]) - int(each[1]))

            x_direction = int(copysign(1, int(each[2]) - int(each[0])))
            y_direction = int(copysign(1, int(each[3]) - int(each[1])))

            start_X = int(each[0])
            start_Y = int(each[1])
            end_X = int(each[3])
            end_Y = int(each[2])

            for i in range(0, distance_x+1):
                # if start_X == start_Y:
                valve_list[start_Y+i*y_direction][start_X+i*x_direction] = int(
                    valve_list[start_Y+i*y_direction][start_X+i*x_direction])+1
                # elif

            # for i in range(min(int(each[0]), int(each[2])), max(int(each[0]), int(each[2]))+1):
            #     # for j in range(min(int(each[1]), int(each[3])), max(int(each[1]), int(each[3]))+1):
            #     if int(each[1]) == int(each[2]):
            #         valve_list[i+max_diag_1][i+max_daig_2] = int(
            #             valve_list[i+int(each[1])][i+int(each[1])]) + int(1)
            #     elif int(each[0]) == int(each[2])+distance:
            #         valve_list[i+distance][i+distance] = int(
            #             valve_list[i+distance][i+distance]) + int(1)

    for i in range(len(valve_list)):
        valve_list[i] = list(filter(lambda x: x > 1, valve_list[i]))

    valve_list = list(filter(None, valve_list))
    sum = 0
    for i in range(len(valve_list)):
        sum += len(valve_list[i])

    # for i in range(len(clear_list)):
    # print(clear_list[i].split(",")[0])
    # print(clear_list[i].split(",")[3])

    return sum


def day_6(file_name, number_of_days: int):
    # open and read file with data

    with open(file_name) as f:
        lines = f.readlines()
    f.close()
    # convert from string to integer
    initial_laternFish = [eval(i) for i in list(lines[0].split(","))]
    # initial_length = len(initial_laternFish)
    # adults = 0

    # initialization variables used later in code.
    lf_day_8 = 0
    lf_day_7 = 0
    temp_day_6 = 0
    lf_day_6 = initial_laternFish.count(6)
    lf_day_5 = initial_laternFish.count(5)
    lf_day_4 = initial_laternFish.count(4)
    lf_day_3 = initial_laternFish.count(3)
    lf_day_2 = initial_laternFish.count(2)
    lf_day_1 = initial_laternFish.count(1)
    lf_day_0 = initial_laternFish.count(0)
    sum_adults = lf_day_0+lf_day_1+lf_day_2+lf_day_3+lf_day_4+lf_day_5+lf_day_6

    for i in range(number_of_days+1):
        temp_day_6 = 0
        if lf_day_7 > 0:
            temp_day_6 += lf_day_7
            lf_day_7 = 0
        if lf_day_8 > 0:
            lf_day_7 = lf_day_8
            sum_adults += lf_day_8
            lf_day_8 = 0

        if lf_day_0 > 0:
            lf_day_8 = lf_day_0
            temp_day_6 += lf_day_0
            lf_day_0 = 0
        if lf_day_1 > 0:
            lf_day_0 = lf_day_1
            lf_day_1 = 0
        if lf_day_2 > 0:
            lf_day_1 = lf_day_2
            lf_day_2 = 0
        if lf_day_3 > 0:
            lf_day_2 = lf_day_3
            lf_day_3 = 0
        if lf_day_4 > 0:
            lf_day_3 = lf_day_4
            lf_day_4 = 0
        if lf_day_5 > 0:
            lf_day_4 = lf_day_5
            lf_day_5 = 0
        if lf_day_6 > 0:
            lf_day_5 = lf_day_6
            lf_day_6 = 0

        lf_day_6 += temp_day_6
        # # first version not very efective due to nested loops and extending list
        # # using above solution dramatically reduce time necessary to made proper calculations

        # initial_length = len(initial_laternFish)

        # for j in range(initial_length):
        #     if initial_laternFish[j] == 0:
        #         adults += 1
        #         initial_laternFish[j] = 6
        #         initial_laternFish.append(8)

        #     elif initial_laternFish[j]:
        #         initial_laternFish[j] -= 1

    return (sum_adults)


def day_7(file_name):

    t_start = time.time()
    with open(file_name) as f:
        lines = f.readlines()
    f.close()
    initial_points = [eval(i) for i in lines[0].split(',')]
    sum = 0
    #
    # Using statistics for better understanding of what happened in process
    #
    var = np.nanmedian(initial_points)
    sum = function(initial_points, var)
    # for i in range(len(initial_points)):

    #     sum += abs(initial_points[i]-var)
    t_end = time.time()
    print(round(t_end - t_start, 3))
    # second part
    min_var = 0
    sum = function_2(initial_points, var)
    for i in range(max(initial_points)):
        temp_sum = function_2(initial_points, var)
        if temp_sum < sum:
            sum = temp_sum
            min_var = var
        var += 1
    return sum, min_var


def function(list, value: int):
    sum = 0
    for each in list:
        sum += abs(each - value)
    return sum


def function_2(list, value: int):
    sum = 0
    difference = 0
    for each in list:
        difference = abs(each - value)
        sum += (difference+1)*difference/2
    return sum


def day_8(file_name):

    with open(file_name) as f:
        lines = f.readlines()
    f.close()
    output_lines = [each.replace('\n', '') for each in lines]
    # second approach
    # declaration of all using list
    signal_list = []
    decode_list = []
    generated_numbers = []

    code = [0]*4
    number = [0]*8
    for each in output_lines:
        ControlString = []
        signal_code = each.split('|')
        signal_code[1] = signal_code[1].strip()
        signal_list = each.split('|')[0].split(' ')
        signal_list.sort(key=len)
        signal_list = [item for item in signal_list if len(item) > 0]
        decode_list = []
        final_number_list = []
        # convert letter to number to write each numebr in binary format
        for each in signal_list:
            number = convert_string_to_binary(each)
            decode_list.append(number)

        topDash = [el1 - el2 for (el1, el2)
                   in zip(decode_list[1], decode_list[0])]
        leftUpperAndMiddleDashes = [el1 - el2 for (el1, el2)
                                    in zip(decode_list[2], decode_list[0])]
        five = [el1+el2 for (el1, el2) in zip(topDash,
                                              leftUpperAndMiddleDashes)]

        for i in range(3, 6):
            sum_ones = np.sum(
                np.array([el1-el2 for (el1, el2) in zip(decode_list[i], five)]) == 1, axis=0)
            second_sum_ones = np.sum(np.array(
                [el1-el2 for (el1, el2) in zip(decode_list[i], decode_list[0])]) == 1, axis=0)
            if sum_ones == 2:
                decode_list[i][0] = 5
                five_list = decode_list[i]
            elif second_sum_ones == 3:
                decode_list[i][0] = 3
                three = decode_list[i]
            else:
                decode_list[i][0] = 2
        # check how many lines stay visible when we deduct 5 and 3 from checke number.
        for j in range(6, 9):
            sum_ones_three = np.sum(
                np.array([el1-el2 for (el1, el2) in zip(decode_list[j], three)]) == 1, axis=0)
            sum_ones_five = np.sum(
                np.array([el1-el2 for (el1, el2) in zip(decode_list[j], five_list)]) == 1, axis=0)
            if sum_ones_three == 1 and sum_ones_five == 1:
                decode_list[j][0] = 9
            elif sum_ones_three == 2 and sum_ones_five == 2:
                decode_list[j][0] = 0
            elif sum_ones_three == 2 and sum_ones_five == 1:
                decode_list[j][0] = 6
        decode_list.sort()

        # prepare list of numbers and binary representation on display.
        ControlString = [''.join(map(str, each)) for each in decode_list]

        for each in signal_code[1].split(' '):
            each = convert_string_to_binary(each)
            each = each[1:]
            each = ''.join(map(str, each))
            filter_obj = list(
                filter(lambda str1: each in str1[1:], ControlString))
            final_number_list.append(filter_obj[0])

        code = [each[0] for each in final_number_list]
        generated_numbers.append(''.join(map(str, code)))

    final_sum = sum(map(int, generated_numbers))

    onces = 0
    fources = 0
    eightes = 0
    sevences = 0
    general_sum = 0
    for each in output_lines:
        temp1 = sum(len(x) == 2 for x in list(each.split(' ')))
        temp4 = sum(len(x) == 4 for x in list(each.split(' ')))
        temp8 = sum(len(x) == 7 for x in list(each.split(' ')))
        temp7 = sum(len(x) == 3 for x in list(each.split(' ')))
        onces += temp1
        fources += temp4
        eightes += temp8
        sevences += temp7

    general_sum = onces+fources+eightes+sevences
    return final_sum


def convert_string_to_binary(inputString):
    number = [0]*8
    if len(inputString) == 2:
        number[0] = 1
        number[ord(inputString[0])-96] = 1
        number[ord(inputString[1])-96] = 1
    elif len(inputString) == 3:
        number[0] = 7
        number[ord(inputString[0])-96] = 1
        number[ord(inputString[1])-96] = 1
        number[ord(inputString[2])-96] = 1
    elif len(inputString) == 4:
        number[0] = 4
        number[ord(inputString[0])-96] = 1
        number[ord(inputString[1])-96] = 1
        number[ord(inputString[2])-96] = 1
        number[ord(inputString[3])-96] = 1
    elif len(inputString) == 7:
        number[0] = 8
        number[ord(inputString[0])-96] = 1
        number[ord(inputString[1])-96] = 1
        number[ord(inputString[2])-96] = 1
        number[ord(inputString[3])-96] = 1
        number[ord(inputString[4])-96] = 1
        number[ord(inputString[5])-96] = 1
        number[ord(inputString[6])-96] = 1
    elif len(inputString) == 5:
        number[0] = 235
        number[ord(inputString[0])-96] = 1
        number[ord(inputString[1])-96] = 1
        number[ord(inputString[2])-96] = 1
        number[ord(inputString[3])-96] = 1
        number[ord(inputString[4])-96] = 1
    elif len(inputString) == 6:
        number[0] = 690
        number[ord(inputString[0])-96] = 1
        number[ord(inputString[1])-96] = 1
        number[ord(inputString[2])-96] = 1
        number[ord(inputString[3])-96] = 1
        number[ord(inputString[4])-96] = 1
        number[ord(inputString[5])-96] = 1
    return number


def day_9(file_name):
    final_rezult = 0
    matrix_to_check = []
    point = []
    difference = []
    risk_level = 0
    with open(file_name) as f:
        lines = f.readlines()
    f.close()

    lines = [each.replace('\n', '') for each in lines]
    # map matrix from string to int.
    for each in lines:
        matrix_to_check.append(list(map(int, each)))
    # select funnels in solution part 1 of day 9
    # for i in range(len(matrix_to_check)):
    #     if i == 0:
    #         difference = [
    #             el1 - el2 for (el1, el2) in zip(matrix_to_check[i], matrix_to_check[i+1])]
    #         for j in range(len(matrix_to_check[i])):
    #             if difference[j] < 0:
    #                 if j == 0 and matrix_to_check[i][j] < matrix_to_check[i][j+1]:
    #                     point.append(matrix_to_check[i][j])
    #                 elif j == len(matrix_to_check[i])-1 and matrix_to_check[i][j-1] > matrix_to_check[i][j]:
    #                     point.append(matrix_to_check[i][j])
    #                 elif matrix_to_check[i][j] < matrix_to_check[i][j+1] and matrix_to_check[i][j-1] > matrix_to_check[i][j]:
    #                     point.append(matrix_to_check[i][j])
    #     elif i == len(matrix_to_check)-1:
    #         difference = [
    #             el1 - el2 for (el1, el2) in zip(matrix_to_check[i], matrix_to_check[i-1])]
    #         for j in range(len(matrix_to_check[i])):
    #             if difference[j] < 0:
    #                 if j == 0 and matrix_to_check[i][j] < matrix_to_check[i][j+1]:
    #                     point.append(matrix_to_check[i][j])
    #                 elif j == len(matrix_to_check[i])-1 and matrix_to_check[i][j-1] > matrix_to_check[i][j]:
    #                     point.append(matrix_to_check[i][j])
    #                 elif j < len(matrix_to_check[i])-1 and matrix_to_check[i][j-1] > matrix_to_check[i][j] and matrix_to_check[i][j+1] > matrix_to_check[i][j]:
    #                     point.append(matrix_to_check[i][j])
    #     else:
    #         difference = [
    #             el1 - el2 for (el1, el2) in zip(matrix_to_check[i], matrix_to_check[i-1])]
    #         difference_1 = [
    #             el1 - el2 for (el1, el2) in zip(matrix_to_check[i], matrix_to_check[i+1])]

    #         for j in range(len(matrix_to_check[i])):
    #             if difference[j] < 0 and difference_1[j] < 0:
    #                 if j == 0 and matrix_to_check[i][j] < matrix_to_check[i][j+1]:
    #                     point.append(matrix_to_check[i][j])
    #                 elif j == len(matrix_to_check[i])-1 and matrix_to_check[i][j-1] > matrix_to_check[i][j]:
    #                     point.append(matrix_to_check[i][j])
    #                 elif j < len(matrix_to_check[i])-1 and matrix_to_check[i][j-1] > matrix_to_check[i][j] and matrix_to_check[i][j+1] > matrix_to_check[i][j]:
    #                     point.append(matrix_to_check[i][j])
    # second part of solution:
    basines = []
    find_indexes_nine = []
    temp_bas = 0
    temp_basin = []*len(matrix_to_check[0])
    for i in range(len(matrix_to_check)):
        find_indexes_nine.append([k for k, x in enumerate(
            matrix_to_check[i]) if x == 9])  # search for nine to find all positoins of 9's
        for j in range(len(matrix_to_check[i])):
            if matrix_to_check[i][j] < 9:
                matrix_to_check[i][j] = 0
    temp_i = 0
    temp_k = 0
    for i in range(len(matrix_to_check)):
        # if matrix_to_check[i][temp_k] < 9:
        #     temp_bas += 1
        #     if matrix_to_check[i+1][temp_k] < 9:
        #         temp_bas += 1
        temp_i = i
        for j in range(len(matrix_to_check[i])):
            temp_k = j
            while is_less_nine(matrix_to_check[temp_k][temp_i]) == 1:
                if matrix_to_check[temp_k][temp_i] < 9:
                    temp_bas += is_less_nine(matrix_to_check[temp_k][temp_i])
                    matrix_to_check[temp_k][temp_i] = -1
                    temp_k += 1
                elif matrix_to_check[temp_k][temp_i] == 9:
                    temp_i = i+1
                    temp_k = j
            # else:
            #     temp_k = 0
            #     temp_i = i+1

        if j == 0 and temp_bas > 0:
            temp_basin.append(temp_bas)
            temp_bas = 0
            i = temp_i

        #

    risk_level = sum(each+1 for each in point)
    return risk_level


def is_less_nine(number: int):
    if number < 9:
        return 1
    else:
        return 0


def day_10(file_name):

    with open(file_name) as f:
        lines = f.readlines()
    f.close()
    incomplete = True
    lines = [each.replace('\n', '') for each in lines]
    line = []
    opening_brackets = []
    missing_brackets = [0]*4
    incomplete_sequence = []
    wages = [3, 57, 1197, 25137]
    for each_line in lines:
        # print(len(each_line))
        # if len(each_line) % 2 == 0:
        line = list(map(str, each_line))
        opening_brackets = []
        incomplete = True
        # first part of puzzle. - finding corrupted lines.
        for each in line:
            if each == '(' or each == '[' or each == '{' or each == '<':
                opening_brackets.append(each)
            elif ord(opening_brackets[-1]) + 1 == ord(each):
                opening_brackets.pop()
            elif ord(opening_brackets[-1]) + 2 == 62 and ord(each) == 62:
                opening_brackets.pop()
            elif ord(opening_brackets[-1]) + 1 == 41 and ord(each) == 41:
                opening_brackets.pop()
            elif ord(opening_brackets[-1]) + 2 == 93 and ord(each) == 93:
                opening_brackets.pop()
            elif ord(opening_brackets[-1]) + 2 == 125 and ord(each) == 125:
                opening_brackets.pop()
            elif each == ")":
                missing_brackets[0] += 1
                incomplete = False
                break
            elif each == "]":
                missing_brackets[1] += 1
                incomplete = False
                break
            elif each == "}":
                missing_brackets[2] += 1
                incomplete = False
                break
            elif each == ">":
                missing_brackets[3] += 1
                incomplete = False
                break
        # if there is no incorrect bracket it is a incomplete sequence.
        if incomplete:
            incomplete_sequence.append(opening_brackets)
    reverse_incomplete_sequence = []
    temp_sequence = []
    total_sum = []
    # reverse list and sum all values based on given formula
    for each in incomplete_sequence:
        # temp_sequence = each[::-1]
        reverse_incomplete_sequence.append(each[::-1])
    for each in reverse_incomplete_sequence:
        sum = 0
        for i in range(len(each)):
            if each[i] == '{':
                sum = sum*5 + 3
                each[i] = sum
            elif each[i] == '<':
                sum = sum*5 + 4
                each[i] = sum
            elif each[i] == '(':
                sum = sum*5 + 1
                each[i] = sum
            elif each[i] == '[':
                sum = sum*5 + 2
                each[i] = sum
        total_sum.append(max(each))
    total_sum.sort()
    result = total_sum[round(len(total_sum)/2)]
    # result = sum([el1*el2 for el1, el2 in zip(missing_brackets, wages)])
    return result


# def find_boundry(list, k: int):
if __name__ == "__main__":
    file_name = "C:\\Users\\PiotrKoluda\Desktop\\Calendar of code\\Day10Advent calendar.txt"
    # file_name = "C:\\Users\\PiotrKoluda\Desktop\\Calendar of code\\Temp.txt"
    print('result is: {0}'.format(day_10(file_name)))
