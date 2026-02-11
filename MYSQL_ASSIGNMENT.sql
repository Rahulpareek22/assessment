# QUESTION 1) Statement to create the Contact table.

create table contact (
contactid int primary key ,
companyid int ,
foreign key (companyid) references company(companyid) , 
firstname varchar(45),
lastname varchar(45), 
street varchar(45),
city varchar(45) ,
state varchar(2),
zip varchar(10),
ismain boolean ,
email varchar(45) ,
phone varchar(12) 
);

--------------------------------------------------------------------------------------------------------------------------------------
# QUESTION 2) Statement to create the Employee table.

create table employee (
employeeid int primary key ,
firstname varchar(45) ,
lastname varchar(45) ,
salary decimal(10,2) , 
hiredate date ,
jobtitle varchar(25) ,
email varchar(45) ,
phone varchar(12)
) ;

--------------------------------------------------------------------------------------------------------------------------------------
# QUESTION 3) Statement to create the ContactEmployee table.

create table contactemployee (
contactemployeeid int  ,
contactid int ,
foreign key (contactid) references contact(contactid) ,
employeeid int ,
foreign key (employeeid) references employee(employeeid),
 contactdate date ,
descriptionn varchar(100) 
); 
--------------------------------------------------------------------------------------------------------------------------------------
# QUESTION 4) In the Employee table, the statement that changes Lesley Bland’s phone number to 215-555-8800.

update employee set phone = "215-555-8800" where firstname = "Lesley" and lastname = "Bland" ; 

--------------------------------------------------------------------------------------------------------------------------------------
# QUESTION 5) In the Company table, the statement that changes the name of “Urban Outfitters, Inc.” to “Urban Outfitters” .

update company set companyname = "urban outfitters" where companyname = "urban outfitters, inc." ;

--------------------------------------------------------------------------------------------------------------------------------------
# QUESTION 6) In ContactEmployee table, the statement that removes Dianne Connor’s contact event with Jack Lee (one statement).

delete from contactemployee where employeeid = 
( select employeeid from employee where firstname = "Dianne" and lastname = "Connor" )
 and employeeid = ( select employeeid from employee where firstname = "Jack" and lastname = "Lee" );
--------------------------------------------------------------------------------------------------------------------------------------
# QUESTION 7) Write the SQL SELECT query that displays the names of the employees that have contacted Toll Brothers (one statement). Run the SQL SELECT query in MySQL Workbench. Copy the results below as well.

SELECT  employee.employeeid , employee.firstname ,employee.lastname,  company.companyname 
from employee
left JOIN contactemployee ON employee.employeeid = contactemployee.employeeid
right JOIN contact ON contactemployee.contactid = contact.contactid
right JOIN company ON company.companyid = contact.companyid
WHERE company.companyname = "toll brothers " ; 

--------------------------------------------------------------------------------------------------------------------------------------
# QUESTION 8) What is the significance of “%” and “_” operators in the LIKE statement?

 -- the '%' is  used as a wildcard character in my sql .
 -- it used with the 'LIKE' operator.
 -- it Represents one or multiple characters in a string.
 
 -- the "_" is used as a single wildcard character in mysql.
 -- it is also used with the 'like' operator.
 -- it does not represent multiple character like '%' it represent single character in one time. 
--------------------------------------------------------------------------------------------------------------------------------------
# QUESTION 9) Explain normalization in the context of databases. 
 
 -- organizing data into tables called normalization in database. 
 -- creating tables and establishing relationship in tables according to rules   
 -- it removes duplicate data and make database more clear.
--------------------------------------------------------------------------------------------------------------------------------------
# QUESTION 10) What does a join in MySQL mean?
 -- join is used to get relatble rows from two or more tables orr collect common data from different tables  based on common column ,primary key from one table and foreign key from another table .
--------------------------------------------------------------------------------------------------------------------------------------
# QUESTION 11) What do you understand about DDL, DCL, and DML in MySQL?
 -- DML , DCL , DDL are commands in MYSQL. it shows that what type of operation you are performing on tables. 
 -- DDL :- data defination language : CREATE, ALTER, DROP, TRUNCATE
 -- DML :- data manipulation language : SELECT, INSERT, UPDATE, DELETE
 -- DCL :- data control language : GRANT, REVOKE
--------------------------------------------------------------------------------------------------------------------------------------
# question 12) What is the role of the MySQL JOIN clause in a query, and what are some common types of joins?

 -- the main role of MYSQL join in query is to combine common data form two different table in a single table based of a common column in both tables.
 
 -- there are many types of join in MYSQL :- 
 -- INNER JOIN :- Only matching rows from tables
 -- LEFT JOIN :- All from left table and matching row from right table
 -- RIGHT JOIN :- All from right table and matching row from left table 
 -- FULL JOIN :- All from both table
 -- CROSS JOIN :- All combinations
 -- SELF JOIN :- Join a table with itself;
