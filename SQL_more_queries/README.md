# Tasks

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <p>
   <img alt="" loading="lazy" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg" style=""/>
  </p>
  <h2>
   Resources
  </h2>
  <p>
   <strong>
    Read or watch
   </strong>
   :
  </p>
  <ul>
   <li>
    <a href="https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql" target="_blank" title="How To Create a New User and Grant Permissions in MySQL">
     How To Create a New User and Grant Permissions in MySQL
    </a>
   </li>
   <li>
    <a href="https://www.mysqltutorial.org/mysql-grant.aspx" target="_blank" title="How To Use MySQL GRANT Statement To Grant Privileges To a User">
     How To Use MySQL GRANT Statement To Grant Privileges To a User
    </a>
   </li>
   <li>
    <a href="https://zetcode.com/mysql/constraints/" target="_blank" title="MySQL constraints">
     MySQL constraints
    </a>
   </li>
   <li>
    <a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php" target="_blank" title="SQL technique: subqueries">
     SQL technique: subqueries
    </a>
   </li>
   <li>
    <a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php" target="_blank" title="Basic query operation: the join">
     Basic query operation: the join
    </a>
   </li>
   <li>
    <a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php" target="_blank" title="SQL technique: multiple joins and the distinct keyword">
     SQL technique: multiple joins and the distinct keyword
    </a>
   </li>
   <li>
    <a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php" target="_blank" title="SQL technique: join types">
     SQL technique: join types
    </a>
   </li>
   <li>
    <a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php" target="_blank" title="SQL technique: union and minus">
     SQL technique: union and minus
    </a>
   </li>
   <li>
    <a href="https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf" target="_blank" title="MySQL Cheat Sheet">
     MySQL Cheat Sheet
    </a>
   </li>
   <li>
    <a href="https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html" target="_blank" title="The Seven Types of SQL Joins">
     The Seven Types of SQL Joins
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=yPu6qV5byu4" target="_blank" title="MySQL Tutorial">
     MySQL Tutorial
    </a>
   </li>
   <li>
    <a href="https://www.sqlstyle.guide/" target="_blank" title="SQL Style Guide">
     SQL Style Guide
    </a>
   </li>
   <li>
    <a href="https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html" target="_blank" title="MySQL 8.0 SQL Statement Syntax">
     MySQL 8.0 SQL Statement Syntax
    </a>
   </li>
  </ul>
  <p>
   Extra resources around relational database model design:
  </p>
  <ul>
   <li>
    <a href="https://www.guru99.com/database-design.html" target="_blank" title="Design">
     Design
    </a>
   </li>
   <li>
    <a href="https://www.guru99.com/database-normalization.html" target="_blank" title="Normalization">
     Normalization
    </a>
   </li>
   <li>
    <a href="https://www.guru99.com/er-modeling.html" target="_blank" title="ER Modeling">
     ER Modeling
    </a>
   </li>
  </ul>
  <h2>
   Learning Objectives
  </h2>
  <p>
   At the end of this project, you are expected to be able to
   <a href="https://fs.blog/feynman-learning-technique/" target="_blank" title="explain to anyone">
    explain to anyone
   </a>
   ,
   <strong>
    without the help of Google
   </strong>
   :
  </p>
  <h3>
   General
  </h3>
  <ul>
   <li>
    How to create a new MySQL user
   </li>
   <li>
    How to manage privileges for a user to a database or table
   </li>
   <li>
    What’s a
    <code>
     PRIMARY KEY
    </code>
   </li>
   <li>
    What’s a
    <code>
     FOREIGN KEY
    </code>
   </li>
   <li>
    How to use
    <code>
     NOT NULL
    </code>
    and
    <code>
     UNIQUE
    </code>
    constraints
   </li>
   <li>
    How to retrieve datas from multiple tables in one request
   </li>
   <li>
    What are subqueries
   </li>
   <li>
    What are
    <code>
     JOIN
    </code>
    and
    <code>
     UNION
    </code>
   </li>
  </ul>
  <h2>
   Requirements
  </h2>
  <h3>
   General
  </h3>
  <ul>
   <li>
    Allowed editors:
    <code>
     vi
    </code>
    ,
    <code>
     vim
    </code>
    ,
    <code>
     emacs
    </code>
   </li>
   <li>
    All your files will be executed on Ubuntu 20.04 LTS using
    <code>
     MySQL 8.0
    </code>
    (version 8.0.25)
   </li>
   <li>
    All your files should end with a new line
   </li>
   <li>
    All your SQL queries should have a comment just before (i.e. syntax above)
   </li>
   <li>
    All your files should start by a comment describing the task
   </li>
   <li>
    All SQL keywords should be in uppercase (
    <code>
     SELECT
    </code>
    ,
    <code>
     WHERE
    </code>
    …)
   </li>
   <li>
    A
    <code>
     README.md
    </code>
    file, at the root of the folder of the project, is mandatory
   </li>
   <li>
    The length of your files will be tested using
    <code>
     wc
    </code>
   </li>
  </ul>
  <h2>
   More Info
  </h2>
  <h3>
   Comments for your SQL file:
  </h3>
  <pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>
  <h3>
   Install MySQL 8.0 on Ubuntu 20.04 LTS
  </h3>
  <pre><code>$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
</code></pre>
  <p>
   Connect to your MySQL server:
  </p>
  <pre><code>$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql&gt;
mysql&gt; quit
Bye
$
</code></pre>
  <h3>
   Use the sandbox to run MySQL
  </h3>
  <p>
   <strong>
    In the container, credentials are
    <code>
     root/root
    </code>
   </strong>
  </p>
  <ul>
   <li>
    Ask for container
    <code>
     Ubuntu 20.04
    </code>
   </li>
   <li>
    Connect via SSH
   </li>
   <li>
    OR connect via the Web terminal
   </li>
   <li>
    In the container, you should start MySQL before playing with it:
   </li>
  </ul>
  <pre><code>$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
</code></pre>
  <p>
   <strong>
    In the container, credentials are
    <code>
     root/root
    </code>
   </strong>
  </p>
  <h3>
   How to import a SQL dump
  </h3>
  <pre><code>$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
</code></pre>
  <p>
   <img alt="" loading="lazy" src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20221114%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20221114T135934Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=bbf5db8b7ffe59dc737b3a312614ae3575b9019ef6b36432d7d8b72cdd46d7c8" style=""/>
  </p>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/2129)
</html>