-- 4.7
use university019;
create table employee(
    p_name varchar(20),
    street varchar(20),
    city varchar(20),
    primary key(p_name)
);

create table works(
    p_name varchar(20),
    c_name varchar(20),
    salary integer,
    primary key(p_name),
    foreign key(p_name) references employee,
    foreign key(c_name) references company
);

create table company(
    c_name varchar(20),
    city varchar(20),
    primary key(c_name)
);

create table manages(
    p_name varchar(20),
    m_name varchar(20),
    primary key(p_name),
    foreign key(p_name) references employee,
    foreign key(p_name) references employee
)

insert into employee values
    ('a','x','sz'),
    ('b','z','sz'),
    ('c','y','xa'),
    ('d','w','xa');

insert into company values
    ('tx','sz'),
    ('bd','xa');

insert into works values
    ('a','tx',10000),
    ('b','tx',12000),
    ('c','bd',9000),
    ('d','bd',20000);

insert into manages values
    ('a','m1'),
    ('b','m1'),
    ('c','m2');

-- 4.12
select employee.p_name
from manages right join employee
on manages.p_name=employee.p_name
where m_name is null;

