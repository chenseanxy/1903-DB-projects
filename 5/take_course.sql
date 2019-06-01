DELIMITER //
create trigger take_course_on_take_insert
after insert on take019 for each row
begin	
	declare cr int;
	declare insert_type int;
	set cr=(select crs_cr from course019 where crs_id=new.crs_id);
	set insert_type=(select crs_type from course019 where crs_id=new.crs_id);
	
    update student019
	set req_cr = req_cr + cr
	where new.stu_id=stu_id and new.score<60 and insert_type=1;    #Required
	
    update student019
	set restr_cr = restr_cr + cr
	where new.stu_id=stu_id and new.score<60 and insert_type=2;    #Restricted
	
    update student019
	set opt_cr = opt_cr + cr
	where new.stu_id=stu_id and new.score<60 and insert_type=3;    #Optional
end//
DELIMITER ;