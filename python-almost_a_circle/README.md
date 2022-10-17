# Tasks

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <h2>
   Background Context
  </h2>
  <p>
   The AirBnB project is a big part of the Higher level curriculum. 
This project will help you be ready for it.
  </p>
  <p>
   In this project, you will review everything about Python:
  </p>
  <ul>
   <li>
    Import
   </li>
   <li>
    Exceptions
   </li>
   <li>
    Class
   </li>
   <li>
    Private attribute
   </li>
   <li>
    Getter/Setter
   </li>
   <li>
    Class method
   </li>
   <li>
    Static method
   </li>
   <li>
    Inheritance
   </li>
   <li>
    Unittest
   </li>
   <li>
    Read/Write file
   </li>
  </ul>
  <p>
   You will also learn about:
  </p>
  <ul>
   <li>
    <code>
     args
    </code>
    and
    <code>
     kwargs
    </code>
   </li>
   <li>
    Serialization/Deserialization
   </li>
   <li>
    JSON
   </li>
  </ul>
  <video autoplay="" loop="">
   <source src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/331/giphy.mp4" type="video/mp4"/>
  </video>
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
    <a href="https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/" target="_blank" title="args/kwargs">
     args/kwargs
    </a>
   </li>
   <li>
    <a href="https://docs.python.org/3/library/json.html" target="_blank" title="JSON encoder and decoder">
     JSON encoder and decoder
    </a>
   </li>
   <li>
    <a href="https://docs.python.org/3.4/library/unittest.html#module-unittest" target="_blank" title="unittest module">
     unittest module
    </a>
   </li>
   <li>
    <a href="https://www.pythonsheets.com/notes/python-tests.html" target="_blank" title="Python test cheatsheet">
     Python test cheatsheet
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
    What is Unit testing and how to implement it in a large project
   </li>
   <li>
    How to serialize and deserialize a Class
   </li>
   <li>
    How to write and read a JSON file
   </li>
   <li>
    What is
    <code>
     *args
    </code>
    and how to use it
   </li>
   <li>
    What is
    <code>
     **kwargs
    </code>
    and how to use it
   </li>
   <li>
    How to handle named arguments in a function
   </li>
  </ul>
  <h2>
   Requirements
  </h2>
  <h3>
   Python Scripts
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
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
   </li>
   <li>
    All your files should end with a new line
   </li>
   <li>
    The first line of all your files should be exactly
    <code>
     #!/usr/bin/python3
    </code>
   </li>
   <li>
    A
    <code>
     README.md
    </code>
    file, at the root of the folder of the project, is mandatory
   </li>
   <li>
    Your code should use the pycodestyle (version 2.7.*)
   </li>
   <li>
    All your files must be executable
   </li>
   <li>
    The length of your files will be tested using
    <code>
     wc
    </code>
   </li>
   <li>
    All your modules should be documented:
    <code>
     python3 -c 'print(__import__("my_module").__doc__)'
    </code>
   </li>
   <li>
    All your classes should be documented:
    <code>
     python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    </code>
   </li>
   <li>
    All your functions (inside and outside a class) should be documented:
    <code>
     python3 -c 'print(__import__("my_module").my_function.__doc__)'
    </code>
    and
    <code>
     python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    </code>
   </li>
   <li>
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
   </li>
  </ul>
  <h3>
   Python Unit Tests
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
    All your files should end with a new line
   </li>
   <li>
    All your test files should be inside a folder
    <code>
     tests
    </code>
   </li>
   <li>
    You have to use the
    <a href="https://docs.python.org/3.4/library/unittest.html#module-unittest" target="_blank" title="unittest module">
     unittest module
    </a>
   </li>
   <li>
    All your test files should be python files (extension:
    <code>
     .py
    </code>
    )
   </li>
   <li>
    All your test files and folders should start with
    <code>
     test_
    </code>
   </li>
   <li>
    Your file organization in the tests folder should be the same as your project: ex: for
    <code>
     models/base.py
    </code>
    , unit tests must be in:
    <code>
     tests/test_models/test_base.py
    </code>
   </li>
   <li>
    All your tests should be executed by using this command:
    <code>
     python3 -m unittest discover tests
    </code>
   </li>
   <li>
    You can also test file by file by using this command:
    <code>
     python3 -m unittest tests/test_models/test_base.py
    </code>
   </li>
   <li>
    We strongly encourage you to work together on test cases so that you don’t miss any edge case
   </li>
  </ul>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/2211)
</html>