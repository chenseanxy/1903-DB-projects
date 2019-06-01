DELIMITER //
create procedure search_grade(id varchar(20))
BEGIN	
	select crs_id,score
	from take019
	where stu_id=id;
	select AVG(score) as avg_req
	from take019 t,course019 c
	where t.crs_id=c.crs_id and t.stu_id=id and c.crs_type=1;
	select AVG(score) as avg_opt
	from take019 t,course019 c
	where t.crs_id=c.crs_id and t.stu_id=id and c.crs_type<>1;
END//
DELIMITER ;

call search_grade("10001");