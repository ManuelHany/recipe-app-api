#### Test
- the simpletestCase is for tests that require no communication with database
- the testCase is for tests that includes database connection


- in TDD the sequence is as follows: 
  - write test case,
  - make sure it fails
  - implement your code 
  - make sure test case passes


- mocking -> to override or change behavior of dependencies. Avoid uintended side effects and Isolate code bein tested. 
    - for example to mock an e-mail service or a wait time sleep.


- common mistakes:
  - check __init__ module inside test directory
  - check indentation for tests
  - forgetting "test_" prefix. 
  - having both test/ directory and test.py 
  
#### docker run VS docker exec
- docker run: Creates a new container from an image and optionally runs a command in it.
- docker exec -it: Executes a command in an already running container, often used for debugging or interacting with the container.