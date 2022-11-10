-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- in your MySQL server.
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE hbtn_0c_0.first_table.name CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
