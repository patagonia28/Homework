
# coding: utf-8

#создание БД
data = ('иван петров','георгий парфенов','ирина иванова','николай носков','максим радулов','семен слепаков')
import pickle

#проверка, заполнен ли файл
try: 
    f=open('data.pickle', 'rb')
    print(pickle.load(f))
except IOError:
    f=open('data.pickle', 'wb')
    pickle.dump(data, f)


# Создание фильтрации

def func():
    q=input('Что ищете? Введите "Имя" или "Фамилия"')
    i=0
    for n in data:
        a=n.split()
        for b in a:
            if b==q:
                print(a)
                i=i+1
    if i==0:
        print('Попробуйте еще раз')
        func()
        
#запускаем функцию фильтрации
func()

