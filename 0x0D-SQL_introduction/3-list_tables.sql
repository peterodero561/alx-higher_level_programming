-- #!/usr/bin/env bash
-- a script that lists all tables of a database in sql server

DELIMITER $$
DROP PROCEDURE IF EXISTS ListTables;
CREATE PROCEDURE ListTables(IN dbName VARCHAR(255))
BEGIN
	SET @query = CONCAT("USE ", dbName, ";");
	PREPARE stmt FROM @query;
	EXECUTE stmt;
	DEALLOCATE PREPARE stmt;
	SHOW TABLES;
END$$
DELIMITER ;
