----------CRIME REPORT MANAGEMENT SYSTEM--------


---------- DDL STATEMENTS----------

CREATE TABLE crime_details (
  criminal_id int(5) NOT NULL,
  criminal_name varchar(15) NOT NULL,
  criminal_type varchar(15) NOT NULL,
  criminal_NickName varchar(10) Default null,
  crime_Location text NOT NULL,
  crime_date DATE NOT NULL,
  primary key(criminal_id)
);

insert into crime_details VALUES(11,"JOHNSON","MURDERER","jonny","Mandya","1948-07-27");
insert into crime_details VALUES(12,"BERGLIM","ROBBER","berly","Bengaluru","1995-02-05");
insert into crime_details VALUES(13,"ROBERT","SERIAL KILLER","robby","Mangaluru","1999-09-30");
insert into crime_details VALUES(14,"JIMMY","THEIF","jimmy","Nasik","1989-10-22");
insert into crime_details VALUES(15,"STUART","SERIAL KILLER","staum","Dwarka","1967-09-27");
insert into crime_details VALUES(16,"LIMENET","ROBBER","limmy","Delhi","1998-03-23");
insert into crime_details VALUES(17,"USEF","MURDERER","usef","Mumbai","1984-04-17");
insert into crime_details VALUES(18,"MANHAT","THIEF","manhat","Thiruvanathapuram","1967-11-29");

CREATE TABLE crime_fir(
  fir_time TIME NOT NULL,
  case_id varchar(5) NOT NULL,
  fir_date DATE NOT NULL,
  fir_state varchar(15) NOT NULL,
  fir_city varchar(15) NOT NULL,
  primary key(case_id,fir_city)
);

insert into crime_fir VALUES("09:45:34",123,"1967-11-30","Karnataka","Mangaluru");
insert into crime_fir VALUES("14:24:05",453,"1984-04-20","Gujarat","Surat");
insert into crime_fir VALUES("12:45:07",567,"1998-03-25","Tamil Nadu","Kodaikanal");
insert into crime_fir VALUES("05:23:05",234,"1967-09-27","Maharashtra","Nasik");
insert into crime_fir VALUES("07:58:34",668,"1989-10-25","Karnataka","Bengaluru");
insert into crime_fir VALUES("12:49:50",231,"1999-09-30","Gujarat","Dwarka");
insert into crime_fir VALUES("04:56:56",655,"1995-02-07","Andhra Pradesh","Vijayawada");
insert into crime_fir VALUES("22:56:22",111,"1948-07-30","Maharashtra","Mumbai");


CREATE TABLE action_report (
  action_caseid int(5) NOT NULL,
  officer_name varchar(20) NOT NULL,
  officer_id int(5) NOT NULL,
  report_date DATE Default NULL,
  action_evidence varchar(20) Default NULL, 
  action_status varchar(20),
  primary key(action_caseid)
);

insert into action_report VALUES(123,"Ashoka Kumar",2345,"1948-08-30","NULL","NOT Completed");
insert into action_report VALUES(453,"Vinod Chaubey",9854,"1995-03-07","FOUND","COMPLETED");
insert into action_report VALUES(567,"Kempaiah",3673,"1999-10-30","NULL","NOT Completed");
insert into action_report VALUES(234,"M L Kumawat",3562,"1989-11-25","FOUND","COMPLETED");
insert into action_report VALUES(668,"Sanjeev Tripati",2225,"1967-10-27","NULL","NOT Completed");
insert into action_report VALUES(231,"Vijay Salaskar",7363,"1998-04-25","FOUND","COMPLETED");
insert into action_report VALUES(655,"Rakesh Maria",2346,"1984-05-20","NULL","NOT Completed");
insert into action_report VALUES(111,"Chandrappa",6464,"1967-12-30","FOUND","COMPLETED"); 


CREATE TABLE user_details(
  first_name varchar(8) NOT NULL,
  last_name varchar(8) DEFAULT Null,
  user_id int(5) NOT NULL,
  user_address text NOT NULL,
  user_number varchar(10) NOT NULL,
  user_age int(2) NOT NULL,
  primary key(user_id)
);

insert into user_details VALUES("Madhav","Sharma",22,"Maleshwaram 2nd stage",9876543212,22);
insert into user_details VALUES("Lokesh","Vittal",23,"Banshankari 3rd block",9676543212,45);
insert into user_details VALUES("Neeraj","Sharma",24,"Kengeri satellite town",9896543212,39);
insert into user_details VALUES("Pardeep","Dahiya",25,"Banshankari 4rh block",9996543212,18);
insert into user_details VALUES("Sanjeev","Deshmuk",26,"Maleshwaram 1st stage",9336543212,27);
insert into user_details VALUES("Manoj","Prateek",27,"Govindaraja nagara",9876553212,34);
insert into user_details VALUES("Rakesh","Sangroya",28,"Hubli main street",9878843212,56);
insert into user_details VALUES("Chandra","Reddy",29,"Maleshwaram 3rd stage",8876543212,70); 


Create table police_quaters(
  q_city varchar(15) NOT NULL,
  q_state varchar(15) NOT NULL,
  q_number varchar(10) NOT NULL,
  q_address text NOT NULL,
  q_officername varchar(20) NOT NULL,
  q_officerid varchar(5) NOT NULL,
  primary key(q_number,q_officerid,q_officername)
);

insert into police_quaters VALUES("Delhi","Karnataka",9876543211,"Maleshwaram 2nd stage","Ashoka Kumar",2345);
insert into police_quaters VALUES("Bengaluru","Gujarat",9876543212,"Banshankari 3rd block","Vinod Chaubey",9854);
insert into police_quaters VALUES("Mumbai","Maharashtra",8823543212,"Kengeri satellite town","Kempaiah",3673);
insert into police_quaters VALUES("Madur","Tamil Nadu",8876554212,"Banshankari 4rh block","M L Kumawat",3562);
insert into police_quaters VALUES("Dwarka","Andhra Pradesh",8346543212,"Maleshwaram 1st stage","Sanjeev Tripati",2225);
insert into police_quaters VALUES("Mangaluru","Maharashtra",8877543212,"Govindaraja nagara","Vijay Salaskar",7363);
insert into police_quaters VALUES("Nasik","Gujarat",8876599212,"Hubli main street","Rakesh Maria",2346);
insert into police_quaters VALUES("Vijayawada","Tamil Nadu",9976543212,"Maleshwaram 3rd stage","Chandrappa",6464);



delimiter $$
create function crime_arrest(criminal_id varchar(20))
returns varchar(50)
begin
declare print varchar(50);
declare type_crime varchar(20);
type_crime = select criminal_type from crime_details where criminal_id
select type_crime(crime_Location) into type_crime from crime_details where criminal_type = "SERIAL KILLER";
if type_crime > 1 then
set print = "ARREST IMMEDIATELY";
else
set print = "ARREST Later";
end if;
return print;
end$$
delimiter ;

select *, arrest_status from crime_details;






