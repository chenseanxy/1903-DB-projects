DELIMITER //
create PROCEDURE teacher_course(id varchar(15))
BEGIN	
	select crs_id, class_name
	from teach019
	where tchr_id=id;
END//
DELIMITER ;

call teacher_course("10101");