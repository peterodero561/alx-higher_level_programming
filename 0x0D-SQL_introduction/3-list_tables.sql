-- #!/usr/bin/env bash
-- a script that lists all tables of a database in sql server

DELIMETER $$
CREATE PROCEDURE ListTables(IN dbName VARCHAR(255))
BEGIN
	SET @query = CONCAT("USE", dbName, ";");
	PREPARE stmt FROM @query;
	EXECUTE stmt;
	DEALLOCATE PREAPARE stmt;
	SHOW TABLES;
END$$
DELIMETER ;
