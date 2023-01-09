def get_by_date(date, name=None, filename='dump.csv') -> None:
    fields = 'date,open,high,low,close,volume,Name\n'

    file_data = open('sorted_for_date.csv')  # файл с отсортированнными данными
    file_rezult = open(filename, 'w')  # файл для записи результатов
    file_rezult.write(fields)  # запишем шапку
    i = 0
    str = ' '
    if name:  # если есть отбор по имени
        name = ',' + name + '\n'  # чтоб искать полное вхождение по имени
        while str:
            try:
                str = next(file_data)
                if date in str:
                    if name in str:
                        file_rezult.write(str)
                        print(str.strip())
            except:
                str = None
            i += 1
    else:  # если нет отбора по имени
        while str:
            try:
                str = next(file_data)
                if date in str:
                    file_rezult.write(str)
                    print(str.strip())
            except:
                str = None
            i += 1
    file_rezult.close()
    file_data.close()

    return None


if __name__ == '__main__':
    rez = get_by_date(date="2018-01-26", name="PG", filename='dump.csv')

# PS. хм, а с использованием библитотеки CSV и алгоритмом Фибоначи работала в 6 раз медленнее )))
