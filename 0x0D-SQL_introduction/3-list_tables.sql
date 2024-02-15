-- #!/usr/bin/env bash
-- a script that lists all tables of a database in sql server
-- database name will be passed as argument
-- if [ $# -ne 1 ];then
--	echo "Usage: $0 <database>"
--	exit 1
-- fi

-- database=$1

USE mysql; SHOW TABLES;
