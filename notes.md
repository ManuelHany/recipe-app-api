# Start From
- 09 - create user model
  - 05 - normalize user address

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
  
#### docker
- docker run: Creates a new container from an image and optionally runs a command in it.
- docker exec -it: Executes a command in an already running container, often used for debugging or interacting with the container.
- The problem with docker:
  - docker compose make sure the service is started but it doesn't mean that postgres has started for example. 
  - solution is to create custom management wait for db command


#### database
- steps: 

  1. tell django how to connect:
     - Engine (type of database)
     - Hostname (IP or domain name for database)
     - Port
     - Database Name
     - Username
     - Password 
   2. install database adaptor dependencies
   3. update python requirements

- `Psycopg2` is one of the most popular pstgresql adaptor for Python.
- supported by django
- options:
  - psycopg2-binary (ok for dev, not good for production)
  - psycopg2 (compiles from source which means it gets compiled optimized to operating system it's running on but needs its dependencies to be installed) 
- psycopg2 (option 2) is easy with docker, and the list of dependencies: 
  - C compile
  - python3-dev
  - libqp-dev
- equivalent for alpine:
  - postgresql-client
  - build-base
  - postgresql-dev
  - musl-dev

#### user model
- Common Issues:
  - running migrations before setting custom model.
  - Typos in config
  - indentation in manager or model.

- common fields:
  - email     `Emailfield`
  - name      `Charfield`
  - is_active `BooleanField`
  - is_staff  `Booleanfield`

- overriding default django user
  - AbstractBaseUser --> Functionality for auth sys but no any fields
  - PermissionsMixin --> Functionality for permissions feature and all its fields