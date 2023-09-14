# API CRUD operations: Endpoints and Usage

## Create
- _/api_
  * **POST** - Creates/Adds a new `Person`.
    * Required data:
      - name: name of person (name must be string type and unique)
    * Expected response:
      - id: integer id of new `Person`
      - name: name of person
    * Errors:
      > 400: ```{"error":"Name must be a valid string!}``` - if `name` is invalid or not string type.

      > 400: ```{"error":"User (`name`) already exists!}``` - if name is already in use.


    - Sample Usage: curl -X POST http://127.0.0.1:5000/api -H 'Content-Type: application/json' -d '{"name":"Mark Essien"}'
    
    * Response: 
      > `{
      > id = 1,
      > name = "Mark Essien"
      > }`

***

## Read
- _/api/id_
  * **GET** - Fecches details of person with `id`
    * Expected response:
      - id: integer id of new `Person`
      - name: name of person
    * Errors:
      > 404: ```{"error":"Person with id `id` not found!}``` - if user does not exist

      > 404: ```{"error":"Invalid endpoint!"}```  - if `id` is not and integer

    - Sample Usage: curl http://127.0.0.1:5000/api/1

    * Response: 
      > `{
      > id = 1,
      > name = "Mark Essien"
      > }`

***

## Update
- _/api/id_
  * **PUT** - Modifies the details of an existing person
    * Required data:
      - name: name of person (name must be string type and unique)
    * Expected response:
      - id: integer id of new `Person`
      - name: modified name of person
    * Errors:
      > 404: ```{"error":"Invalid endpoint!"}```  - if `id` is not and integer

      > 404: ```{"error":"Person with id `id` not found!}``` - if user does not exist

      > 400: ```{"error":"Name must be a valid string!}``` - if `name` is invalid or not string type.

      > 400: ```{"error":"User (`name`) already exists!}``` - if name is already in use.


    - Sample Usage: curl -X PUT http://127.0.0.1:5000/api/1 -H 'Content-Type: application/json' -d '{"name":"Elon Musk"}'

    * Response: 
      > `{
      > id = 1,
      > name = "Elon Musk"
      > }`
    
***

## Delete
- _/api/id_
  * **DELETE** - Removes/Deletes a person data
    * Errors: 
      > 404: ```{"error":"Invalid endpoint!"}```  - if `id` is not and integer

      > 404: ```{"error":"Person with id `id` not found!}``` - if user does not exist

    - Sample Usage: curl -X DELETE http://127.0.0.1:5000/api/1

    * Response:
      > ```{"message":"Person deleted successfully!}```

***

## Generic error messages

Calls to wrong url/endpoint
> 404: ```{"error":"Invalid endpoint!"}```

Calls with invalid JSON input
> 415: ```{"error":"Not a valid JSON!"}```

Wrong method calls to endpoint
> 405: ```{"error":"Method not allowed for endpoint!"}```

***


## **Note**
> All `Required data` and `Response` are in JSON format.

> `Sample Usage` are for testing the api on the terminal environment. Tools like POSTMAN can also be used.

