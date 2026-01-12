use practice;
show tables;
create table MOVIE (movieid int primary key, moviename varchar(20),category varchar(10), releasedate date,productioncost int, businesscost int);
insert into MOVIE(movieid, moviename, category,releasedate,productioncost,businesscost) values
(001,'Hindi_movie','Musical','2018-04-23',124500,130000),
(002,'Tamil_movie','Action','2016-05-17',112000,118000),
(003,'English_movie','Horror','2017-08-06',245000,360000);
insert into MOVIE(movieid, moviename, category,productioncost) values
(006,'Punjabi_movie','Comedy',30500);
select Category,count(MovieName) from MOVIE GROUP BY Category;
SELECT movieid,moviename, productioncost + businesscost as total_earning from movie;
SELECT movieid,moviename, businesscost-productioncost  as Net_profit from movie where businesscost IS  NOT NULL and productioncost is not null;
SELECT movieid,moviename, productioncost as cost from movie where productioncost BETWEEN 10000 and 100000;
SELECT * from movie where category in ('action','comedy');
SELECT * from movie where releasedate is null;
select * from movie;