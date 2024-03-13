-- creates database hbtn_0d_2 and user_0d_2
-- the user should have only SELECT privilege in the database
-- the user password is user_0d_2_pwd
-- creating database should not fail should the database exist
-- creating user should not fail should the database exist

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
