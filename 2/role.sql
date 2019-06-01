create role dean,instructor;
grant select on teaches019 to instructor;
grant instructor to dean;
create user Tom@'%' identified by  '1234';
create user Ami@'%' identified by  '1234';
grant dean to Tom;
grant select on teaches019 to Tom with grant option;
grant select on teaches019 to Ami;
revoke select on teaches019 from Tom;
