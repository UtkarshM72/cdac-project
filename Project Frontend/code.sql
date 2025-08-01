
CREATE USER 'newuser'@'%' IDENTIFIED BY 'Pass@1234';
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'%';
CREATE DATABASE test1;
USE test1;

CREATE TABLE clients (
id INT AUTO_INCREMENT PRIMARY KEY,
First_Name VARCHAR(30) NOT NULL,
Last_name VARCHAR(30) NOT NULL,
age INT
)
ENGINE=INNODB;

INSERT INTO clients (First_Name, Last_name, age) VALUES ('Keshav', 'Lichade', 23);

CREATE TABLE users (
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(50) NOT NULL UNIQUE,
password VARCHAR(255) NOT NULL,
role VARCHAR(20) DEFAULT 'viewer'
);

INSERT INTO users VALUES(1,"user1","User#123","admin");
INSERT INTO users VALUES(1,"user2","Pass123","viewer");

SELECT * FROM clients;
SELECT * FROM users;
