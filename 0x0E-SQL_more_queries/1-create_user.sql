-- creates a user user_0d_1
-- if user exists it should not fail
-- user_od_1 password is user_0d_1_pwd
-- user_0d_1 should have all privileges

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
