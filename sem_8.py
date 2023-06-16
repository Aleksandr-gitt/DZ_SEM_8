#**********************Телефонный справочник*********************#
import os
 
def showAll():
    with open('DZ_SEM_8\spravo4nik.txt') as file:
        res = [res.strip() for res in file.readlines()]
        print(*res, sep='\n')
 
def addPersonData():
    newPerson = ''
    sonname = input('Введите Фамилию: ')
    firstName = input('Введите Имя: ')
    secondName = input('Введите Отчество: ')
    tel = input('Введите телефон: ')
    res = [sonname,firstName,secondName,tel]
    for i in res:
        newPerson += i + ' '
    return newPerson
 
def phoneBook():
    with open('DZ_SEM_8\spravo4nik.txt') as file:
        phoneBook = [res.strip() for res in file.readlines()]
    return phoneBook
    
def addPerson(fileName,phoneBook,person):
    with open(fileName,'w') as file:
        phoneBook.append(person)
        for i in phoneBook:
            file.write(i+'\n')
    print('Изменения сохранены')
            
def searchData(phoneBook):
    inp = input('Введите запрос для поиска: ')
    res = [i for i in phoneBook if inp in i]
    if res:
        return res
    else:
        return 'МАЗИЛА'
        
def changeData(fileName,phoneBook):
    with open(fileName,'w') as file:
        for i in phoneBook:
            file.write(i+'\n')
    print('Изменения сохранены')
    
def delData(fileName,res):
    a = phoneBook()
    a.remove(res)
    changeData(fileName,a)
 
def changeDelPerson(fileName,phoneBook):
    res = searchData(phoneBook)
    if len(res)>1:
        yourChoice=int(input(f'{res}. Введите порядковый номер записи для действия над ней:'))
        target = res[yourChoice-1]
    phBook = phoneBook
    x = input(f'{target}: Изменить - 1 или Удалить -2 ? ')
    if x == '2':
        delData(fileName,res)
    elif x == '1':
        newPerson = addPersonData()
        for i in range(len(phBook)):
            if target == phBook[i]:
                phBook[i]=newPerson
                changeData(fileName,phBook)
 
def menuData():
    print('''Действия:
        [1] -- Показать весь справочник
        [2] -- Добавить запись             
        [3] -- Поиск
        [4] -- Редактирование
        [5] -- Выход
        ''')
    enterNum = input()
    if enterNum == '1':       # Весь справочник
        showAll()
        print()
        menuData()
    elif enterNum == '2':   # Добавление
        addPerson('DZ_SEM_8\spravo4nik.txt',phoneBook(),addPersonData())
        print()
        menuData()
    elif enterNum == '3':     # Поиск
        print(searchData(phoneBook()))
        print()
        menuData()
    elif enterNum == '4':    # Удаление или правка
        changeDelPerson('DZ_SEM_8\spravo4nik.txt',phoneBook())
        print()
        menuData()
    elif enterNum == '5':
        exit
    else:
        print('При выборе в меню, у тебя 10 ошибок из 1 возможной. Давай сначала')
        menuData()
    
 
print('Я уже начал скучать по тебе...')
print()
menuData()