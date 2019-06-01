create view compsci_detail as
select course019.course_id, sec_id, building, room_no
from course019, section019
where course019.course_id=section019.course_id
	and course019.Dept_name='Comp. Sci. '
	and section019.Semester='Spring'
	and section019.Year=2010;