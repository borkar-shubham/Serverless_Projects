## Create API
### Use the following format input for testing the API
```
{
    "tasktype":"create",
    "data":{
         "id": "1",
         "name": "Putin",
         "breed": "Joe",
         "gender": "male",
         "owner": "Trump",
         "birthday": "2012-05-15"
    }
  }
  
  {
    "tasktype":"read",
    "data":{
         "id": "1"
    }
  }
  
  {
    "tasktype":"update",
    "data":{
         "id": "1",
         "name": "Harry",
         "breed": "Joe",
         "gender": "Male",
         "owner": "Mike",
         "birthday": "2012-05-15"
    }
  }
  
  {
    "tasktype":"delete",
    "data":{
         "id": "1"
    }
  }
  ```
