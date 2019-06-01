DELIMITER //
create procedure stu_teacher(id varchar(20))
BEGIN	
	select distinct ts.tchr_name
	from teach019 te, take019 ta ,teacher019 ts
	where te.crs_id=ta.crs_id and ts.tchr_id=te.tchr_id and ta.stu_id=id;
END//
DELIMITER ;

call stu_teacher("10002");