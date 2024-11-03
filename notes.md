# Start From
- 14 Build Recipe API
  - 7 Write tests for deleting ingredients

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

- Public and Private tests:
  - public tests are tests that do not require authentication. 
  - private tests are those that do require authentication.
  
#### docker
- docker run: Creates a new container from an image and optionally runs a command in it.
- docker exec -it: Executes a command in an already running container, often used for debugging or interacting with the container.
- docker compose run --rm app sh -c "python manage.py <command>"
- The problem with docker:
  - docker compose make sure the service is started but it doesn't mean that postgres has started for example. 
  - solution is to create custom management wait for db command
  - th PYTHONUNBUFFERED env is used to directly buffer or python logs and prints to be visivle in docker logs.
- `ARG` vs `ENV`:
  - Unlike ENV, which sets environment variables available at runtime (inside the container), ARG is only available during the image build process. Once the image is built, the ARG variable is no longer accessible inside the running container.


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

#### APIs documentation
- What to doccument?
  1. Available endpoints (paths) -> `/api/recipes`
  2. Supported methods -> `Get'` `Post`, `PUT`, `PATCH`, `DELETE`
  3. Format of payloads (inputs)
     - parameters
     - post json format
  4. Format of responses (outputs) -> Response JSON format
  5. Authentication process


#### Django
- Serializers
  -  a way to convert objects to and from python objects. 
  - it takes json input it validates it
  - convert it into a python object or a model into our database.
  - automatically validate and save things into a specific model

- Serializers VS Nested Serializers:
  - are often used to represent related models, and both serializers.Serializer and serializers.ModelSerializer support nesting, though ModelSerializer makes it easier when working with model-based relationships.
      1. Serializers.ModelSerializer (srializers) is used to map exactly the constrains inside the models itself like the CharField and everything.
      2. Serializers.Serializer gives you full control but requires manual field definitions and methods.

- class Meta:
  - this is where we tell django rest the model and the fields and additional arguments that we want to pass to the serializer.

- Authentication:
  - Basic -> send username and passweord with each request.
  - Token -> Use a token in the HTTP header. store on clinet (session storage, local storage, cookie or database)
  - JSON Web Token (JWT) -> Use an access and refresh token (super scalable) to minimize requests
  - Session -> Use cookies

- APIView vs VIEWSets
  - -> a view is what handles a request made to a certain URL.
  - `APIView`
    1. Focused around HTTP methods.
    2. class methods for HTTP -> GET, POST, PUT PATCH, DELETE
    3. Provide flexibility over URLs and logic 
    4. Useful for NON CRUD APIs: 
      - eg: authentication, jobs, external apis.
      - anything that doesn't map to a specific model in your system.
  - `Viewsets`
    1. focused around actions -> Retrieve, list, update, partial updated, destroy
    2. Map to django models
    3. Use routers to generate URLs
    4. Great for CRUD operations on models.

- `mixins`
  - mixins are mainly things that you could mix in to a view to add functionality.

#### Python
- setattr:
  - The `setattr` function in Python is used to set the value of an attribute of an object dynamically. It takes three arguments: 
  1. `object`: The object whose attribute is being set.
  2. `attribute name`: The name of the attribute you want to set (as a string).
  3. `value`: The value to assign to the attribute.
