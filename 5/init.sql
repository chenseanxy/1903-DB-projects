create database school019;
use school019;

create table department019(
    dept_name varchar(20),
    primary key(dept_name)
);
create table profession019(
    prof_name varchar(20),
    dept_name varchar(20),
    primary key(prof_name),
    foreign key(dept_name) references department019(dept_name)
);
create table class019(
    class_name varchar(20),
    prof_name varchar(20),
    primary key(class_name),
    foreign key(prof_name) references profession019(prof_name)
);
create table course019(
    crs_id varchar(20),
    crs_name varchar(100),
    crs_type int,
    crs_cr int,
    primary key(crs_id),
    constraint crs_type_chk check (crs_type in (1,2,3))
);
create table teacher019(
    tchr_id varchar(20),
    tchr_name varchar(20), 
    dept_name varchar(20),
    primary key(tchr_id),
    foreign key(dept_name) references department019(dept_name)
);
create table teach019(
    tchr_id varchar(20),
    class_name varchar(20),
    crs_id varchar(20),
    primary key(tchr_id, class_name),
    foreign key(tchr_id) references teacher019(tchr_id),
    foreign key(class_name) references class019(class_name),
    foreign key(crs_id) references course019(crs_id)
);
create table student019(
    stu_id varchar(20),
    stu_name varchar(20),
    gender char(1),
    term char(2),
    req_cr int,
    restr_cr int,
    opt_cr int,
    class_name varchar(20),
    primary key(stu_id),
    foreign key(class_name) references class019(class_name),
    constraint stu_sex_chk check (gender in ("M","F")),
    constraint stu_term_chk check (term in ("1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B"))
);
create table take019(
    stu_id varchar(20),
    crs_id varchar(20),
    score int,
    term char(2),
    primary key(stu_id, crs_id),
    foreign key(stu_id) references student019(stu_id),
    foreign key(crs_id) references course019(crs_id),
    constraint score_chk check (score>=0 and score<=100),
	constraint study_term_chk check (term in ("1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B"))
);
