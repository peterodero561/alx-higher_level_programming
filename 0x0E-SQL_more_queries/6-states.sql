-- creates database hbtn_0d_usa and table states
-- states atrributes are id INT autogenarated cant be null and is primary
-- key and name VARCHAR() can't be null
-- if database exists it should not fail
-- if table exists it should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
