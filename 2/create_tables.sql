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

CREATE TABLE CLASSROOM019(
    building varchar (20),
    room_no varchar (20),
    capacity numeric (4,0),
    primary key(building, room_no)
);

CREATE TABLE SECTION019(
	course_id  varchar(20),
	sec_id  varchar(20),
	semester varchar(20),
	year numeric(4),
	building  varchar(15),
	room_no varchar(20),
	time_slot_id varchar(10),
	primary key(course_id, sec_id, semester, year),
	constraint section_year_chk check(year<=2100 and year>=2000),
    foreign key(building, room_no) references CLASSROOM019(building, room_no)
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

CREATE TABLE STUDENT019(
    ID varchar(20),
    name varchar(20),
    dept_name varchar(20),
    tot_cred int,
    primary key(ID),
	foreign key(dept_name) references DEPARTMENT019(dept_name)
);

CREATE TABLE TAKES019(
	ID varchar(20),
	course_id varchar(20),
	sec_id varchar(20),
	semester varchar(20),
	year numeric(4),
	grade varchar(5),
	primary key(ID, course_id, year),
	constraint take_year_chk check(year<=2100 and year>=2000),
	foreign key(course_id, sec_id, semester, year) references SECTION019(course_id, sec_id, semester, year)
);

CREATE TABLE ADVISOR019(
	student_ID varchar(15),
 	instructor_ID varchar(15),
	primary key(student_ID, instructor_ID),
	foreign key(student_ID) references STUDENT019(ID),
	foreign key(instructor_ID) references INSTRUCTOR019(ID)
);

CREATE TABLE TIME_SLOT019(
	time_slot_id varchar(20), 
	day varchar(20), 
	start_time varchar(20), 
	end_time varchar(20)
);

show tables;
