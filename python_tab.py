import os

path_dir = './'
file_list = os.listdir(path_dir)
file_list.sort()
temp_list = []

while True:
    word = input()
    word_temp = list(word)
    count = 0

    if word_temp[len(word_temp) - 1] == '\t':
        word = word[0 : len(word) - 1]
        print(word)
        for file in file_list:
            file.lower()
            if file.find(word, 0, len(word)) != -1:
                count = count + 1
                temp_list.append(file)
    
    if len(temp_list) >= 2:
        for file in temp_list:
            print(file)
        print('------------')
    
    elif len(temp_list) == 1:
        print(temp_list[0])
        stat = os.stat(temp_list[0])
        print(stat)
        if stat[0] == 33204:
            if temp_list[0].endswith('.py'):
                os.system('python3 ' + temp_list[0])
            elif temp_list[0].endswith('.cpp') or temp_list[0].endswith('.c'):
                os.system('./' + temp_list[0])
            break

    temp_list.clear()


