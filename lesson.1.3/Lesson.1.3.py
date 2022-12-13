from time import sleep
from unittest import expectedFailure
import requests
from bs4 import BeautifulSoup
import json
import tqdm 
import string
from traceback import print_tb


#1. Cпарсить данные о вакансиях python разработчиков с сайта hh.ru 
def parse_it():
    dict_period = {
    'Нет опыта': 'noExperience',
    'От 1 года до 3 лет':'between1And3',
    'От 3 до 6 лет': 'between3And6',
    'Более 6 лет': 'moreThan6'}
                
    headers = {'accept': '*/*',
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.2.1495 Yowser/2.5 Safari/537.36"}

    parse_of_date = {
        "data": []
    }

    for exp in range(len(dict_period)):    
        base_url = f'https://stavropol.hh.ru/search/vacancy?experience={list(dict_period.values())[exp]}&search_field=name&search_field=company_name&search_field=description&text=python+разработчик&items_on_page=20'
        response = requests.get(base_url, headers = headers)
        soup = BeautifulSoup(response.text, "lxml")

        for item in range(0, int(soup.find('div', {'class':'pager'}).find_all(attrs={'data-qa':'pager-page'})[-1].text)):
            url_page = base_url + '&page={item}'
            resp = requests.get(url_page, headers = headers)
            soup = BeautifulSoup(resp.text, "lxml")

            for element in tqdm.tqdm(soup.find_all('div', {'class':"serp-item"})):
                title = element.find('a', {'class':'serp-item__title'}).text
                work_exp = list(dict_period.keys())[exp]
                region = element.find(attrs={'data-qa':'vacancy-serp__vacancy-address'}).text 
                try:
                    salary = element.find(attrs={"data-qa":"vacancy-serp__vacancy-compensation"}).text
                except:
                    salary = None
                parse_of_date['data'].append({'title': title, 'work experience': work_exp, 'salary': salary, "region": region})
                
                with open('Lesson.1.3.json', "w", encoding ='utf8') as file:
                    json.dump(parse_of_date, file, ensure_ascii=False)

            sleep(10)

#2. Палиндром строки
def check_palindrome():
    print("Введите строку для получения полиндрома")
    word = input()
    word1 = str(word).replace(' ', '')
    if str(word1) == str(word1)[::-1] :
        print("true")
    else:
        print("false")

#3. Перевод арабского числа в римское
def checkio():
    print("Введите год для трансформации")
    data = input()
    n1 = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    n10 = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    n100 = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    n1000 = ["","M","MM","MMM","MMMM"]
    
    t = n1000[data // 1000]
    h = n100[data // 100 % 10]
    te = n10[data // 10 % 10]
    o =  n1[data % 10]
    print (t+h+te+o)

#4. Валидность скобок
def balanced():
    print("Введите последовательность скобок")
    text = input()
    brackets="()[]{}"
    opening, closing = brackets[::2], brackets[1::2]
    stack = [] 
    for character in text:
        if character in opening: 
            stack.append(opening.index(character))
        elif character in closing: 
            if stack and stack[-1] == closing.index(character):
                stack.pop()  
            else:
                print("Последовательность не валидна")
                return
                #return False # unbalanced (no corresponding opening bracket) or
                             # unmatched (different type) closing bracket
    if not stack: 
        print("Последовательность валидна")
    else:
        print("Последовательность не валидна")
    #return (not stack) # no unbalanced brackets

#5. Умножить два бинарных числа в формате строк
def bin_mul():
    print ("Введите первое двоичное число Х1=")
    x1 = input()
    print ("Введите второе двоичное число Х2=")
    x2 = input()
    print("\n" + str(bin(int(x1, 2) * int(x2, 2))))

def printHead():
    print('Выберите номер задачи из списка (0-для выхода):')
    print('1. Cпарсить данные о вакансиях python разработчиков с сайта hh.ru')
    print('2. Палиндром строки')
    print('3. Перевод арабского числа в римское')
    print('4. Валидность скобок')
    print('5. Умножить два бинарных числа в формате строк')
    return int(input())

# Основной цикл программы
solve = printHead()
while solve != 0:
    match solve:
        case 0:
            break
        case 1:
            parse_it()
        case 2:
            check_palindrome()
        case 3:
            checkio()
        case 4:
            balanced()
        case 5:
            bin_mul()
        case _:
            print('Выбрано неверное значение. Попробуйте снова\n')
    solve = printHead()