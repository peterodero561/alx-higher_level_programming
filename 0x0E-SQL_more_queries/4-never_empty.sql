-- creates the table id_not_null
-- it has atrributes id default value 1, name VARCHAR(256)
-- if table exists it should not fail

CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1 NOT NULL,
	name VARCHAR(256)
);
