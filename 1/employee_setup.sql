create database l1_employee;
use l1_employee;

create table employee(
	employee_name varchar(60),
    street varchar(60),
    city varchar(30),
    primary key(employee_name)
);

create table company(
	company_name varchar(60),
    city varchar(30),
    primary key(company_name)
);

create table works(
	employee_name varchar(60),
    company_name varchar(60),
    salary numeric(10,2),
    primary key(employee_name),
    check(salary > 0),
    foreign key(employee_name) references employee(employee_name),
    foreign key(company_name) references company(company_name)
);

create table manages(
	employee_name varchar(60),
    manager_name varchar(60),
    primary key(employee_name),
    foreign key(employee_name) references employee(employee_name),
    foreign key(manager_name) references employee(employee_name)
);

show tables;
