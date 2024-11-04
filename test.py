with open('1.txt', encoding="utf-8") as file1:
    line_count1 = 0
    read_f1 = ''
    for line in file1:
        read_f1 += line
        line_count1 += 1

with open('2.txt', encoding="utf-8") as file2:
    line_count2 = 0
    read_f2 = ''
    for line in file2:
        read_f2 += line
        line_count2 += 1

    # print(line_count2)

with open('3.txt', 'w', encoding="utf-8") as file3:
    if line_count1 < line_count2:
        file3.write(f'1.txt\n{line_count1}\n{read_f1}\n')
        file3.write(f'2.txt\n{line_count2}\n{read_f2}')
    else:
        file3.write(f'2.txt\n{line_count2}\n{read_f2}\n')
        file3.write(f'1.txt\n{line_count1}\n{read_f1}')
    