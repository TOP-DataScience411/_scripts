def count_inf(start, ascending=True):
    step = ascending or -1
    while True:
        yield start
        start += step



def user_enumerate(iterable, start=0, ascending=True):
    gen_obj = count_inf(start, ascending)
    for elem in iterable:
        yield (gen_obj.__next__(), elem)


books = [
    "Apeltsin. Data Science Bookcamp.pdf", 
    "Campesato. Pandas Basics.pdf", 
    "Downey. Think Bayes.pdf", 
    "Halvorsen. Python for Science and Engineering.pdf", 
    "Lerner. Pandas Workout. 200 exercises.pdf", 
    "Брюс, Гедек. Практическая статистика для специалистов Data Science.pdf", 
    "Будума. Основы глубокого обучения.pdf", 
    "Васильев. Обработка естественного языка.pdf", 
    "Вирсански. Генетические алгоритмы на Python.pdf", 
    "Джоши. Искусственный интеллект с примерами на Python.pdf", 
    "Дэвидсон-Пайлон. Вероятностное программирование на Python.pdf", 
    "Коэн. Прикладная линейная алгебра для исследователей данных.pdf", 
    "Лонца. Алгоритмы обучения с подкреплением на Python.pdf", 
    "Маккинни. Python и анализ данных.pdf", 
    "Мартин. Байесовский анализ на Python.pdf", 
    "О'Нил, Шатт. Data Science.pdf", 
    "Омельяненко. Эволюционные нейросети на языке Python.pdf", 
    "Плас. Python для сложных задач.pdf", 
    "Постолит. Основы искусственного интеллекта в примерах на Python.pdf", 
    "Протодьяконов, Пылов, Садовников. Алгоритмы Data Science и их практическая реализация на  Python.pdf",
    "Титов, Тазиева. Решение задач линейной алгебры и прикладной математики в Python.pdf", 
    "Траск. Грокаем глубокое обучение.pdf", 
    "Трофимов. Библиотека NumPy.pdf", 
    "Хайкин. Нейронные сети.pdf", 
    "Харрисон. Машинное обучение. Карманный справочник.pdf", 
    "Хилл. Научное программирование на Python.pdf", 
    "Хобсон, Ханнес, Коул. Обработка естественного языка в действии.pdf", 
    "Шолле. Глубокое обучение на Python.pdf", 
    "Элбон. Машинное обучение с использованием Python.pdf"
]
for n, book in user_enumerate(books, len(books), False):
    print(f'{n}. {book}')


