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


if __name__ == "__main__":
    # file_name = "C:\\Users\\PiotrKoluda\Desktop\\Calendar of code\\Day10Advent calendar.txt"
    file_name = "C:\\Users\\PiotrKoluda\Desktop\\Calendar of code\\Temp.txt"
    print('result is: {0}'.format(day_1_2022(file_name)))
