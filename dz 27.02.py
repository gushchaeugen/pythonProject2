eng = 'qwertyuiopasdfghjklzxcvbnm'
rus = 'юбьтимсчяфывапролджэъхзщшгнекуцйё'

li_en = {1 : 'A, E, I, O, U, L, N, S, T, R' ,
        2 : 'D, G' ,
        3 : 'B, C, M, P' ,
        4 : 'F, H, V, W, Y' ,
        5 : 'k' ,
        8 : 'J, X' ,
        10 : 'Q, Z'}

li_ru = {1 : 'А, В, Е, И, Н, О, Р, С, Т' ,
        2 : 'Д, К, Л, М, П, У' ,
        3 : 'Б, Г, Ё, Ь, Я' ,
        4 : 'Й, Ы' ,
        5 : 'Ж, З, Х, Ц, Ч' ,
        8 : 'Ш, Э, Ю' ,
        10 : 'Ф, Щ, Ъ'}

a = input('введите слово: ')

if a[0].lower() in eng:
        summa = 0
        for letter in a:
                for key, value in li_en.items():
                        if letter.upper() in value:
                                summa += key
        print(f'стоимость введённого англ слова = {summa}')
else:
    if a[0].lower() in rus:
        summa = 0
        for letter in a:
                for key, value in li_ru.items():
                        if letter.upper() in value:
                             summa += key
        print(f'стоимость введённого русского слова = {summa}')

