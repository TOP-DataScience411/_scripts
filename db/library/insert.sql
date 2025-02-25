-- insert into authors (last_name, first_name) values ("Азимов", "Айзек");

-- insert into authors (last_name, first_name) 
-- values ("Азимов", "Айзек");

insert into authors 
  (first_name, last_name) 
values 
  ("Айзек", "Азимов"); 

insert into authors values (4, "Брэдбери", "Рэй");

insert into authors 
  (first_name, last_name) 
values 
  ("Лев", "Толстой"),
  ("Михаил", "Булгаков"),
  ("Константин", "Циолковский"),
  ("Мария", "Семёнова"),
  ("Сергей", "Лукьяненко"),
  ("Лоис", "Буджолд"),
  ("Сергей", "Булгаков");


insert into publishers
  (name)
values
  ("АСТ"),
  ("Эксмо");

insert ignore into publishers
  (name)
values
  ("Азбука"),
  ("Эксмо");


insert into books
  (author_id, title)
values
  ( 1, "Основание"),
  ( 1, "Край Основания"),
  ( 4, "Вино из одуванчиков"),
  ( 4, "Марсианские хроники"),
  ( 4, "Электрическое тело, пою!"),
  ( 5, "Война и мир"),
  ( 6, "Мастер и Маргарита"),
  ( 7, "Путь в космос"),
  ( 8, "Истовик-камень"),
  ( 9, "Спектр"),
  ( 9, "Осенние визиты"),
  (10, "Барраяр"),
  (10, "Ученик воина"),
  (11, "Свет невечерний");


