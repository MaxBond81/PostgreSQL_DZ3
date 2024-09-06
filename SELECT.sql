
--Задание 2--

SELECT "name", length FROM tracks
WHERE length = (SELECT MAX(length) FROM tracks);

SELECT "name", length FROM tracks
WHERE length >= 210;

SELECT "name" FROM collections
WHERE release_year BETWEEN 2018 AND 2020;

SELECT "name" FROM singers
WHERE "name" NOT LIKE '% %';

SELECT "name" FROM tracks
WHERE "name" LIKE '%мой%' OR "name" LIKE '%my%';

--Заданние 3--

SELECT "name",COUNT(singer_id) FROM genresinger gs
JOIN genres g ON gs.genre_id = g.genre_id 
GROUP BY g."name" 
ORDER BY count(singer_id) DESC;


SELECT a."name" ,COUNT(t.album_id) FROM tracks t
JOIN albums a ON t.album_id = a.album_id 
WHERE a.release_year BETWEEN 2019 AND 2020
GROUP BY a.album_id; 

SELECT a."name", AVG(t.length) FROM tracks t
JOIN albums a ON t.album_id = a.album_id 
GROUP BY a.album_id; 

SELECT s."name" FROM albumsinger a2
JOIN singers s ON a2.singer_id = s.singer_id 
JOIN albums a ON a2.album_id = a.album_id
WHERE a.release_year != 2020
GROUP BY s."name" ;

SELECT c."name" FROM trackcollection tc
JOIN collections c ON tc.collection_id = c.collection_id 
JOIN tracks t ON tc.track_id = t.track_id 
JOIN albums a ON t.album_id = a.album_id
JOIN albumsinger asg ON a.album_id = asg.album_id
JOIN singers s ON asg.singer_id = s.singer_id 
WHERE s."name" = 'Александр Новиков'
GROUP BY c."name";

--Задание 4 --

SELECT a."name", COUNT(gs.singer_id) FROM albums a 
JOIN albumsinger asg ON a.album_id = asg.album_id 
JOIN singers s ON asg.singer_id = s.singer_id
JOIN genresinger gs ON s.singer_id = gs.singer_id
GROUP BY a."name"
HAVING COUNT(*) > 1;

SELECT t."name" FROM tracks t 
LEFT JOIN trackcollection tc ON t.track_id = tc.track_id 
LEFT JOIN collections c ON tc.collection_id = c.collection_id 
GROUP BY t."name"
HAVING COUNT(tc.collection_id) = 0;

SELECT s."name", MIN(t.length) FROM tracks t 
JOIN albums a ON t.album_id = a.album_id 
JOIN albumsinger asg ON a.album_id = asg.album_id
JOIN singers s ON asg.singer_id = s.singer_id
WHERE t.length = (SELECT MIN(length) FROM tracks)
GROUP BY s."name";

SELECT a."name", count(t.album_id) FROM albums a 
JOIN tracks t  ON a.album_id = t.album_id
GROUP BY a."name"
HAVING count(t.album_id) = (SELECT MIN(COUNT) FROM (SELECT a."name", count(t.album_id) FROM albums a 
JOIN tracks t  ON a.album_id = t.album_id GROUP BY a."name"));
