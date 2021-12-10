# 🔥 Scrum Board Sprint 6 #2 🔥
meeting time: 2021.12.08

Daily standup meeting, report of progress and difficulties


### Team Member #1:

**Name**:
Jordan Belinsky, 18JMB16, 20164936

**Branch**:
backend_purchase

**Progress**:
Completed implementation of the purchase functionality, and ensured that it is compatible with the rest of the tests and models predefined.

**Difficulties**:
As mentioned in the previous meeting, the product model we had already created was not setup properly to support the purchase functionality. So a difficulty was determining how to properly modify the product model (which ended up with adding a boolean isSold and a user email input) to fix this contingency issue.

**Plan**:
No direct plan is applicable at this point, aside from being available for questions from other group members, ready for PR reviews, and approvals.


### Team Member #2:

**Name**:
Winfred Tai, 17zt12, 20103850

**Branch**:
frontend_dev_deploy

**Progress**:
finished the implementation of new menu, but meanwhile need to modify the backend models and add more helper functions in models.py file which is not supposed to be done by frontend devs.

**Difficulties**:
almost all the .in and .out files need to be re-written as menu has changed a little bit, and output has the relatively obvious change, huge amount of work needs to be done to fix the frontend test. 

**Plan**:
I would share work with Arthur otherwise there would be too much testing cases to implement.
### Team Member #3:

**Name**:
Sizhe Guan, 17sg46, 20090459

**Branch**:
bacend_security_test

**Progress**:
I have designed a few test cases for checking the buyer's email and owner's email, checking balance before placing orders and 
checking if the product is sold out

**Difficulties**:
The backend deployment should be able to set the is_sold attribute default to false and the user who creates this product should be able to change its state into true when the product is actually sold out. 

**Plan**:
Gonna design other test cases for product sold out situation once the backend modify the create product and update production functions.


### Team Member #4:

**Name**:
Ziyuan Yu, 16zy18, 20032445

**Branch**:


**Progress**:


**Difficulties**:


**Plan**:




