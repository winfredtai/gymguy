# 🔥 Scrum Board Sprint 6 🔥
meeting time: 2021.12.06

Daily standup meeting, report of progress and difficulties


### Team Member #1:

**Name**:
Jordan Belinsky, 18JMB16, 20164936

**Branch**:
backend_purchase

**Progress**:
Designed the general structure for the backend function using pseudo code. Planning out how the function is best implemented, and how the connections to the rest of the program will properly work.

**Difficulties**:
The main difficulty encountered is that our pre-established Product class/model was not setup to work properly with the purchasing of items, and thus has to be modified in order to properly connect.

**Plan**:
Add relevant functions to the Product class, followed by creating a purchase function which will take a user and product object and update attributes according to the instructions given.


### Team Member #2:

**Name**:
Winfred Tai, 17zt12, 20103850

**Branch**:
frontend_dev_deploy

**Progress**:
Just started to design testing cases and re-construct the logic of CLI menu, have come up with the sketch of the test cases followed the same template as sprint 4, .in file has been constructed for tests later, however, not yet finished the .out file as it requires the implmentation of frontend CLI menu.

**Difficulties**:
It reuires much additonal work to fit the CLI menu to the new functionalities, as well as the connectin bewtween it and backend models. 

**Plan**:
Need to finish frontend logic as soon as possible so that the testing cases could be finised based on that. Deployment through docker also requires the implementation of the whole system, including all the tests.


### Team Member #3:

**Name**:
Sizhe Guan, 17sg46, 20090459

**Branch**:
backend_security_test

**Progress**:
I am just having ideas about how to test the newly added features. The job of testing is built on the foundation of backend feature deployment and our backend developer has just finished the function design. 

**Difficulties**:
The placing order functionality is associated with both user and product database. The testing samples should follow the construction restrictions of two object models. Also there are many attributes related, I need to create lots of test cases to run through all possibilities.

**Plan**:
Planning to add true and false sample cases for each attribute of placing orders feature. The security testing is similar as the one we did before. It should pass since our implementation doesn’t conclude and SQL code part.


### Team Member #4:

**Name**:
Ziyuan Yu, 16zy18, 20032445

**Branch**:
Frontend integration testing

**Progress**:
I am just having ideas about how to test the newly added functions of purchasing products. The job of testing is built on the foundation of fronted feature deployment and our frontend developer has just finished the function design. 

**Difficulties**:
The cli interface need to show all available products for users expect sold products, and sold products can be shown to the owner of these products. I need to consider all situation of the interface and test them.

**Plan**:
Planning to check the log for each products and check the products whether it is sold. Then check the user page which can show all of products which created by the owner with both sold and available.



