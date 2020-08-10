-- Creates the database database hbnb_dev_db in the MySQL server
-- Creates a new user 'hbnb_dev' (in localhost) with password of 'hbnb_dev_pwd'
-- hbnb_dev should have all privileges on the database hbnb_dev_db
-- hbnb_dev should have SELECT privilege on the database performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
