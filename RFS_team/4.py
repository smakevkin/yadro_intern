word = input('Введите нужное слово для поиска: ') #просим слово для поиска

with open('file.txt', 'r') as f: #передаем файл
    for line in f: #смотрим построчно
        if word in line.lower(): #проверка есть ли нужное слово в строке
            print(line) #выводим строку