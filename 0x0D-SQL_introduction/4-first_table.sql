-- A script that creates a table called "first_table" in caurrent database
-- it has id and name

DELIMITER $$
CREATE PROCEDURE CreateFirstTable()
BEGIN
	-- DECLARE CONTINUE HANDLER FOR SQLEXEPTION BEGIN END;
	CREATE TABLE IF NOT EXISTS first_table (
		id INT,
		name VARCHAR(256)
	);
END$$
DELIMITER ;
