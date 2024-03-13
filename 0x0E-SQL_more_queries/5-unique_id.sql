-- creates a table unique_id
-- has atrributes id INT default 1 and must be unique, nameVARCHAR()
-- if table exists it should not fail

CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 NOT NULL PRIMARY KEY,
	name VARCHAR(256)
);
