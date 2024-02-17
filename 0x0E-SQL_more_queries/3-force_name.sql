-- creates a table force_name
-- table has atrributes id INT, name VARCHAR(256) not null
-- if table exists it should not fail

CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
);
