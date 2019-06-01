create table student(
	sno varchar(5),
	sname varchar (10),
	primary key(sno)
);

create table course(
	cno varchar(5),
	cname varchar(10),
	primary key(cno)
);

create table sc(
	s_no varchar(5),
	c_no varchar(10),
	primary key(s_no,c_no),
	foreign key(s_no) references student(sno),
	foreign key(c_no) references course(cno)
);
