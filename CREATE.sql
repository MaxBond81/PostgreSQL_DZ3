CREATE TABLE IF NOT EXISTS Genres (
	genre_id SERIAL PRIMARY KEY,
 	name VARCHAR(60) NOT NULL
); 
 
 CREATE TABLE IF NOT EXISTS Singers (
 	singer_id SERIAL PRIMARY KEY,
 	name VARCHAR(60) NOT NULL
 );
 
CREATE TABLE IF NOT EXISTS GenreSinger (
 	genre_id INTEGER REFERENCES Genres(genre_id),
 	singer_id INTEGER REFERENCES Singers(singer_id),
 			  CONSTRAINT pk_1 PRIMARY KEY(genre_id,singer_id) 
 );
 
 CREATE TABLE IF NOT EXISTS Albums (
 	album_id SERIAL PRIMARY KEY,
 	name VARCHAR(60) NOT NULL,
 	release_year SMALLINT NOT NULL CHECK(release_year > 1900)
 );
 
CREATE TABLE IF NOT EXISTS AlbumSinger (
 	album_id INTEGER REFERENCES Albums (album_id),
 	singer_id INTEGER REFERENCES Singers(singer_id),
 			  CONSTRAINT pk_2 PRIMARY KEY(album_id,singer_id)
 );

 CREATE TABLE IF NOT EXISTS Tracks (
 	track_id SERIAL PRIMARY KEY,
 	name VARCHAR(60) NOT NULL,
 	length INTEGER NOT NULL CHECK(length > 10 AND length < 600),
 	album_id INTEGER NOT NULL REFERENCES Albums (album_id)
 );
 
CREATE TABLE IF NOT EXISTS Collections (
 	collection_id SERIAL PRIMARY KEY,
 	name VARCHAR(60) NOT NULL,
 	release_year SMALLINT NOT NULL CHECK(release_year > 1900)
 );
 
CREATE TABLE IF NOT EXISTS TrackCollection (
 	track_id INTEGER REFERENCES TrackS(track_id),
 	collection_id INTEGER REFERENCES CollectionS(collection_id),
 				  CONSTRAINT pk_3 PRIMARY KEY(track_id,collection_id) 
 );