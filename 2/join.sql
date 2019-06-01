select * from student019 s natural inner join takes019 t;

select * from student019 s left outer join takes019 t on t.ID=s.ID;

select * from student019 s right outer join takes019 t on t.ID=s.ID;

select * from student019 s left outer join takes019 t on t.ID=s.ID
union(select * from student019 a right outer join takes019 b on b.ID=a.ID);
