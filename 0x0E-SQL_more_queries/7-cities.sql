-- creates database hbtn_0d_usa and table cities
-- cities attributes are id INT, states_id INT forign key referencing
-- states table, name VARCHAR() not null
-- if database exists it should not fail
-- if table exists it should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	states_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (states_id) REFERENCES states(id)
);
