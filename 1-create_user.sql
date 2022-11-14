-- creates the MySQL server user user_0d_1.
CREATE IF NOT EXISTS USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
