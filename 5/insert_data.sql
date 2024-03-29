insert into department019 values
	('Biology'),
    ('EECS'),
	('Finance'),
	('History'),
	('Music'),
	('Physics');
insert into profession019 values
    ('Molecular Bio.', 'Biology'),
    ('Human Bio.', 'Biology'),
    ('Comp. Sci.', 'EECS'),
    ('Elec. Eng.', 'EECS'),
    ('Finance', 'Finance'),
    ('History', 'History'),
    ('Music', 'Music'),
    ('Physics', 'Physics');
insert into class019 values
    ('BIO-MB', 'Molecular Bio.'),
    ('BIO-HB', 'Human Bio.'),
    ('CS-01', 'Comp. Sci.'),
    ('EE-01', 'Elec. Eng.'),
    ('FIN-01', 'Finance'),
    ('HIS-01', 'History'),
    ('MU-01', 'Music'),
    ('PHY-01', 'Physics');
insert into course019 values
	('BIO-101', 'Intro. to Biology', 1, 4),
	('BIO-301', 'Genetics', 2, 4),
	('BIO-399', 'Computational Biology', 3, 3),
	('CS-101', 'Intro. to Computer Science', 1, 4),
	('CS-190', 'Game Design', 2, 4),
	('CS-315', 'Robotics', 3, 3),
	('CS-319', 'Image Processing', 2, 3),
	('CS-347', 'Database System Concepts', 3, 3),
	('EE-181', 'Intro. to Digital Systems', 1, 3),
	('FIN-201', 'Investment Banking', 2, 3),
	('HIS-351', 'World History', 1, 3),
	('MU-199', 'Music Video Production', 3, 3),
	('PHY-101', 'Physical Principles', 1, 4);
insert into teacher019 values
	('10101', 'Srinivasan', 'EECS'),
	('12121', 'Wu', 'Finance'),
	('15151', 'Mozart', 'Music'),
	('22222', 'Einstein', 'Physics'),
	('32343', 'El Said', 'History'),
	('33456', 'Gold', 'Physics'),
	('45565', 'Katz', 'EECS'),	
    ('45568', 'Matt', 'EECS'),
	('58583', 'Califieri', 'History'),
	('76543', 'Singh', 'Finance'),
	('76766', 'Crick', 'Biology'),
	('76767', 'Dean', 'Biology'),
	('83821', 'Brandt', 'EECS'),
	('98345', 'Kim', 'EECS');
insert into teach019 values
    ('76766', 'BIO-MB', 'BIO-101'),
	('76767', 'BIO-MB', 'BIO-301'),
    ('76766', 'BIO-HB', 'BIO-101'),
	('76767', 'BIO-HB', 'BIO-399'),
	('10101', 'CS-01', 'CS-101'),
	('45565', 'CS-01', 'CS-190'),
	('45568', 'CS-01', 'CS-315'),
	('83821', 'CS-01', 'CS-319'),
	('98345', 'CS-01', 'CS-347'),
	('83821', 'EE-01', 'EE-181'),
	('12121', 'FIN-01', 'FIN-201'),
	('32343', 'HIS-01', 'HIS-351'),
	('15151', 'MU-01', 'MU-199'),
	('33456', 'PHY-01', 'PHY-101');
insert into student019 values
    ('10000','Olson','M','3A',7,9,1,'CS-01'),
    ('10001','Cuadros','F','4B',1,6,6,'CS-01'),
    ('10002','Earle','F','2B',10,7,1,'BIO-HB'),
    ('10003','Rock','M','3B',21,7,5,'EE-01'),
    ('10004','Ramin','M','3B',14,3,5,'MU-01'),
    ('10005','Morris','F','1B',8,4,2,'BIO-MB'),
    ('10006','Clark','F','1A',22,2,1,'PHY-01'),
    ('10007','Walker','F','1B',1,8,8,'MU-01'),
    ('10008','Sutherland','F','1A',7,4,5,'FIN-01'),
    ('10009','Brooks','F','2A',1,3,4,'EE-01'),
    ('10010','Smith','M','3B',6,8,9,'HIS-01'),
    ('10011','Hyder','M','1B',15,6,1,'EE-01'),
    ('10012','Cromwell','M','3A',0,5,4,'BIO-HB'),
    ('10013','Hylan','F','3B',10,2,4,'BIO-MB'),
    ('10014','Hart','M','2A',17,6,8,'CS-01'),
    ('10015','Avino','M','4B',12,5,4,'CS-01'),
    ('10016','Thomas','F','1A',28,9,5,'CS-01'),
    ('10017','Mikelson','M','3B',29,8,8,'BIO-HB'),
    ('10018','Weiss','F','2B',24,6,6,'HIS-01'),
    ('10019','Stultz','F','3A',28,0,7,'HIS-01');
insert into take019 values
    ('10000','CS-315',67,'3B'),
    ('10001','CS-315',97,'3A'),
    ('10002','EE-181',45,'1B'),
    ('10003','PHY-101',75,'1B'),
    ('10004','BIO-399',69,'4B'),
    ('10005','FIN-201',51,'3B'),
    ('10006','PHY-101',87,'3B'),
    ('10007','FIN-201',91,'2B'),
    ('10008','CS-101',93,'1A'),
    ('10009','FIN-201',59,'2B'),
    ('10010','CS-190',73,'1A'),
    ('10011','BIO-399',67,'2B'),
    ('10012','HIS-351',87,'1B'),
    ('10013','CS-101',51,'3B'),
    ('10014','FIN-201',87,'2A'),
    ('10015','CS-190',66,'1A'),
    ('10016','EE-181',90,'3A'),
    ('10017','CS-347',68,'4A'),
    ('10018','CS-190',90,'1B'),
    ('10019','HIS-351',85,'1A');