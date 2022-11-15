-- Database + tables to test
DROP DATABASE IF EXISTS states;
CREATE DATABASE IF NOT EXISTS states;
USE test_1;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("nevada"), ("New York");