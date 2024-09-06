INSERT INTO genres ("name")
VALUES ('shanson'), 
       ('classic'),
       ('new_age'),
	   ('electronic_music'),
	   ('rock');

INSERT INTO singers ("name")
VALUES ('Стас Михайлов'), 
		('Михаил Круг'),
		('Бах'),
		('Моцарт'),
		('Цой'),
		('Vanessa-Mae'),
		('Александр Новиков'),
		('Scorpions'),
		('Karunesh'),
		('Yanni'),
		('Secret Garden');

INSERT INTO genresinger (genre_id, singer_id)
VALUES  (1, 1), 
 		(1, 2),
		(1, 7),
		(2, 3),
		(2, 4),
		(3, 9),
		(3, 10),
		(3, 11),
		(4, 6),
		(4, 10),
		(4, 11),
		(5, 5),
		(5, 8);
	
	
INSERT INTO albums ("name", release_year)
VALUES ('Лирика', 1998), 
		('Стрелочник', 2020),
		('Черный альбом', 1991),
		('Шестое чувство', 2020),
		('In my time', 1993),
		('Crazy World', 1990);	
	
INSERT INTO albumsinger (album_id, singer_id)
VALUES  (1, 2), 
		(2, 7),
		(3, 5),
		(4, 1),
		(5, 10),
		(6, 8);
	
INSERT INTO tracks ("name", length, album_id)
VALUES  ('Мой бог', 205, 1), 
		('Стрелочник', 250, 2),
		('Кукушка', 195, 3),
		('Не отпускай', 180, 4),
		('In my time', 260, 5),
		('Crazy World', 300, 6),
		('Прогулка с месяцем', 185, 1), 
		('Улица восточная', 193, 2),
		('Кончится лето', 320, 3);	

INSERT INTO collections("name", release_year)
VALUES  ('Шансон лучшее', 1998), 
		('Шансон избранное', 2020),
		('Рок 1991', 1991),
		('Instrumental', 2010),
		('Рок лучшее', 2018);	
	
	
INSERT INTO trackcollection(track_id, collection_id)
VALUES  (4, 1),
		(4, 2),
		(5, 2),
		(6, 3),
		(6, 5),
		(7, 2),	
		(8, 4),
		(9, 5),
	    (11,1),
	    (12,5);	
	