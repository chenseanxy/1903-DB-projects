department019(dept_name);
profession019(prof_name, dept_name);
class019(class_name, prof_name);
course019(crs_id, crs_name, crs_type, crs_cr);
teacher019(tchr_id,tchr_name,dept_name);
teach019(tchr_id,class_name,crs_id,term);
student019(stu_id,stu_name,sex,term,req_cr,restr_cr,opt_cr,class_name);
take019(stu_id,crs_id,score);
