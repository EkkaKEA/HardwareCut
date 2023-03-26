# Открываем файл на чтение и запись
with open('Text_A.txt', 'r+') as file:
    # Считываем все строки в список lines
    lines = file.readlines()

    # Создаем пустой список для хранения отфильтрованных строк
    filtered_lines = []

    # Проходимся по каждой строке из списка lines
    for line in lines:
        # Если строка содержит хотя бы одно из слов SLOT, ADDRESS или SYMBOL, добавляем ее в список filtered_lines
        if 'SLOT' in line or 'ADDRESS' in line or 'SYMBOL' in line:
            # Если строка содержит слово ADDRESS, добавляем перед ней строку с разделительной линией
            if 'ADDRESS' in line:
                filtered_lines.append("//------------------------------\n")
            # Удаляем слова LOCAL_IN_ADDRESSES, SYMBOL, LOCAL_OUT_ADDRESSES из строки
            line = line.replace('LOCAL_IN_ADDRESSES', '').replace('SYMBOL', '').replace('LOCAL_OUT_ADDRESSES', '')
            # Добавляем отфильтрованную строку в список filtered_lines
            filtered_lines.append(line)

    # Устанавливаем позицию указателя файла в начало
    file.seek(0)
    # Очищаем содержимое файла
    file.truncate(0)

    # Записываем отфильтрованные строки в файл
    file.writelines(filtered_lines)
