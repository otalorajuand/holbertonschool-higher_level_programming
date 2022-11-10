# Tasks

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <p>
   <img alt="" loading="lazy" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg" style=""/>
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
    <a href="https://www.youtube.com/watch?v=FR4QIeZaPeM" target="_blank" title="What is Database &amp; SQL?">
     What is Database &amp; SQL?
    </a>
   </li>
   <li>
    <a href="https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04" target="_blank" title="A Basic MySQL Tutorial">
     A Basic MySQL Tutorial
    </a>
   </li>
   <li>
    <a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php" target="_blank" title="Basic SQL statements: DDL and DML">
     Basic SQL statements: DDL and DML
    </a>
    (
    <em>
     no need to read the chapter “Privileges”
    </em>
    )
   </li>
   <li>
    <a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php" target="_blank" title="Basic queries: SQL and RA">
     Basic queries: SQL and RA
    </a>
   </li>
   <li>
    <a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php" target="_blank" title="SQL technique: functions">
     SQL technique: functions
    </a>
   </li>
   <li>
    <a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php" target="_blank" title="SQL technique: subqueries">
     SQL technique: subqueries
    </a>
   </li>
   <li>
    <a href="https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458" target="_blank" title="What makes the big difference between a backtick and an apostrophe?">
     What makes the big difference between a backtick and an apostrophe?
    </a>
   </li>
   <li>
    <a href="https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf" target="_blank" title="MySQL Cheat Sheet">
     MySQL Cheat Sheet
    </a>
   </li>
   <li>
    <a href="https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html" target="_blank" title="MySQL 8.0 SQL Statement Syntax">
     MySQL 8.0 SQL Statement Syntax
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
    What’s a database
   </li>
   <li>
    What’s a relational database
   </li>
   <li>
    What does SQL stand for
   </li>
   <li>
    What’s MySQL
   </li>
   <li>
    How to create a database in MySQL
   </li>
   <li>
    What does
    <code>
     DDL
    </code>
    and
    <code>
     DML
    </code>
    stand for
   </li>
   <li>
    How to
    <code>
     CREATE
    </code>
    or
    <code>
     ALTER
    </code>
    a table
   </li>
   <li>
    How to
    <code>
     SELECT
    </code>
    data from a table
   </li>
   <li>
    How to
    <code>
     INSERT
    </code>
    ,
    <code>
     UPDATE
    </code>
    or
    <code>
     DELETE
    </code>
    data
   </li>
   <li>
    What are
    <code>
     subqueries
    </code>
   </li>
   <li>
    How to use MySQL functions
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
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/2128)
</html>