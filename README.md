# Tasks
GraphQL API server example.

It uses an in-memory data store, so the data resets after each server restart.

## Usage

### Start
Running the API: `python run.py`

### General
- Endpoint: `<server>/graphql`
- Method: `POST`
- Headers: `Content-Type`: `application/json`

### Body

Query all tasks
```graphql
{
    "query": "{ tasks { title completed } }"
}
```

Query one task
```graphql
{
    "query": "query($t:String!){ task(title:$t){ title completed } }",
    "variables": { "t": "Learn Graphene" }
}
```

Add a new task
```graphql
{
    "query": "mutation{ addTask(title:\"Buy groceries\"){ success task{ title completed} } }"
}
```

Update a task
```graphql
{
    "query": "mutation{ updateTask(title:\"Buy groceries\", newTitle:\"Buy groceries and snacks\", completed:true){ success task{ title completed} } }"
}
```

Delete a task
```graphql
{
  "query": "mutation{ deleteTask(title:\"Test the API\"){ success deletedTask{ title completed } } }"
}
```

### Return values
- `200` Success
- `400` `"query"` missing
- `415` Request not JSON

### Testing
The folder `postman` includes a Postman collection and environment to test the API.

Notice that, for demonstration purposes, queries with parameters have the latter defined both as body raw parameters and as GraphQL parameters with GraphQL variables.

## Tools
Flask / Graphene / Python

## Author
ChatGPT 5, prompted by Arturo Mora-Rioja, based on [Kesha Williams' repo](https://github.com/LinkedInLearning/programming-foundations-apis-and-web-services-3811153/tree/main/03_02) from her LinkedIn Learning course [*Programming Foundations: APIs and Web Services*](https://www.linkedin.com/learning/programming-foundations-apis-and-web-services-27993033).