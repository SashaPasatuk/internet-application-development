from operator import itemgetter

class Conductor:
#"Дирижер"
    def __init__(self, id, fio, sal, dep_id):

        self.id = id
        self.fio = fio
        self.sal = sal
        self.dep_id = dep_id

class Orchestra:
#"Оркестр"

    def __init__(self, id, name):
        self.id = id
        self.name = name

class CondOr:

#'Дирижеры оркестров' для реализации связи многие-ко-многим

    def __init__(self, dep_id, emp_id):
        self.dep_id = dep_id
        self.emp_id = emp_id

# Оркестры

deps = [
    Orchestra(1, 'оркестр 1'),
    Orchestra(2, 'оркестр 2'),
    Orchestra(3, 'оркестр 3'),
    Orchestra(4, 'оркестр 4'),
    Orchestra(5, 'оркестр 5'),
    Orchestra(6, 'оркестр 6'),
]

# Дирижеры

emps = [
    Conductor(1, 'Абрамов', 30000, 1),
    Conductor(2, 'Петров', 40000, 2),
    Conductor(3, 'Арсеньев', 50000, 3),
    Conductor(4, 'Сидров', 28000, 4),
    Conductor(5, 'Попов', 36000, 3),
    Conductor(5, 'Ибрагимов', 42000, 1)
    ]

emps_deps = [
    CondOr(1,1),
    CondOr(2,2),
    CondOr(3,3),
    CondOr(3,4),
    CondOr(3,5),
    CondOr(5,1),
    CondOr(4,2),
    CondOr(6,3),
    CondOr(6,4),
    CondOr(6,5),
    ]

def main():
#"""Основная функция"""
# Соединение данных один-ко-многим

    one_to_many = [(e.fio, e.sal, d.name)
        for d in deps
        for e in emps
        if e.dep_id==d.id]

# Соединение данных многие-ко-многим

    many_to_many_temp = [(d.name, ed.dep_id, ed.emp_id)
        for d in deps
        for ed in emps_deps
        if d.id==ed.dep_id]
    many_to_many = [(e.fio, e.sal, dep_name)
        for dep_name, dep_id, emp_id in many_to_many_temp
        for e in emps if e.id==emp_id]

    print('Задание А1')
    res_13 = {}
    # Перебираем всех дирижеров
    for d in emps:
        if d.fio[0].lower() == 'а':
            # Список дирижеров
            d_emps = list(filter(lambda i: i[0]==d.fio, one_to_many))
            # название оркестра
            d_emps_names = [x for _,_,x in d_emps]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[d.fio] = d_emps_names
    print(res_13)

    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все оркестры
    for d in deps:
        # Список дирижёров оркестра
        d_emps = list(filter(lambda i: i[2]==d.name, one_to_many))
        # Если отдел не пустой
        if len(d_emps) > 0:
            # Зарплаты дирижеров оркестра
            d_sals = [sal for _,sal,_ in d_emps]
            # Минимальная зарплата дирижера оркестра
            d_sals_min = min(d_sals)
            res_12_unsorted.append((d.name, d_sals_min))
    # Сортировка по минимальной зарплате (по возрастанию)
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=False)
    print(res_12)

    print('\nЗадание А3')
    res1 = {}
    res={}
    # Перебираем всех дирижеров
    for d in emps:
        #Список дирижеров
        d_emps = list(filter(lambda i: i[0]==d.fio, many_to_many))
        # Только название оркестра
        d_emps_names = [x for _,_,x in d_emps]
        # Добавляем результат в словарь
        # ключ - отдел, значение - список оркестров
        res1[d.fio] = d_emps_names
    for k in sorted(res1.keys()):
        res[k]=res1[k]
    print(res)

if __name__ == '__main__':
    main()
