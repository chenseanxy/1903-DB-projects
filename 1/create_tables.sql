use UNIVERSITY019;

CREATE TABLE DEPARTMENT019(
	dept_name  varchar(20),
	building  varchar(15),
	budget  numeric(12,2),
	primary key(dept_name),
	check(budget > 0)
);

CREATE TABLE COURSE019(
	course_id  varchar(20),
	title  varchar(50),
	dept_name  varchar(20),
	credits  numeric(5,1),
	primary key(course_id),
	foreign key(dept_name) references DEPARTMENT019(dept_name),
	check(credits > 0)
);

CREATE TABLE PREREQ019(
	course_id  varchar(20),
	prereq_id  varchar(20),
	primary key(course_id, prereq_id),
	foreign key(course_id) references COURSE019(course_id),
	foreign key(prereq_id) references COURSE019(course_id)  
);

CREATE TABLE INSTRUCTOR019(
	ID varchar(20),
	name  varchar(20),
	dept_name  varchar(20),
	salary  numeric(12,2),
	primary key(ID),
	foreign key(dept_name) references DEPARTMENT019(dept_name),
	check(salary > 0) 
);

CREATE TABLE SECTION019(
	course_id  varchar(20),
	sec_id  varchar(20),
	semester varchar(20),
	year numeric(4),
	building  varchar(15),
	room_no varchar(10),
	time_slot_id varchar(10),
	primary key(course_id, sec_id, semester, year),
	check(semester > 0),
	check(year > 0)
);

CREATE TABLE TEACHES019(
	ID varchar(20),
	course_id  varchar(20),
	sec_id  varchar(20),
	semester varchar(20),
	year numeric(4),
	primary key(ID, course_id, sec_id, semester, year),
	foreign key(ID) references INSTRUCTOR019(ID),
	foreign key(course_id, sec_id, semester, year) references SECTION019(course_id, sec_id, semester, year)
);

show tables;
