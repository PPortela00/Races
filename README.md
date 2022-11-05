# Races

This database creation and manipulation is part of the course Fundamentals of Data Science and Engineering from
FEUP, Faculty of Engineering - University of Porto, and aims at answer the questions propsed and formulating a question (or a
set of questions). 

Below, all the tasks carried out throughout the development of the project will be discussed and what is the importance/component made by the different members:

**UML Diagram (uml.png)** - Regarding the UML and the work that each one carried out at this stage, since this is the starting point of the database and the construction, this was one of the processes that required the most time and attention. We decided that each one would make their own and later we would join, analyse all the diagrams in order to obtain the most complete one that best fits and responds to all cases

**Relational Text (relational.txt)** - The relational model was then carried out following the joint elaboration of the UML diagram.
After the development of the UML diagram it was easy and intuitive to create the relational model based on the knowledge acquired during the course. Briefly, this step was also elaborate together.

**SQL Script for the creation of the DB (races.sql)** - After defining the structure of the database, Miguel was in charge of developing the SQL script that would allow the creation of the database in PostgreSQL, in the public schema, as requested.

**Python Script to manipulate data (load_races.py)** - This represents the most critical process, and undoubtedly the most time consuming, in the development of the entire work. Luis was in charge of developing the code that would manipulate the information for the Database, essentially removing and adding. Since this was an extremely important and hard work stage, the other elements of the group, Miguel and Paulo, also helped in this process. Initially the code was developed for the respective integrations in SQL and later it was integrated and adapted to Python.

**Python Script for the Interface (races.py)** - The development of the interface that would allow the user interaction with the database was in charge of Paulo. An interface was developed that allows the user to inform which connection to the db you want to make (respectively from the 3 developers), which allows you to delete, see basic information from db and add all data to the Database. Whenever the interface - user interation with DB - file is run (races.py), the first interface is called purposely, in which the intended connection and the operations previously identified must be indicated. Posteriorly the final interface is displayed, in which it is possible to view the questions defined by the group and the questions already pré-defined and the respective answer.

**The answer to the 5 question pre-defined (question.sql)** - The elaboration of the answers to the pre-defined questions, the elaboration of both the new questions and the answers to them, were processes carried out by all the members of the group. These represented one of the final steps in which everyone's contribution and mutual help made this process quick and simple.
