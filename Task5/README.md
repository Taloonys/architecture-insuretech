* Entities
```graphql
type Client {
  id: ID!                       # `!` is required ~ non null
  name: String!
  age: Int
  documents: [Document!]!
  relatives: [Relative!]!
}

type Document {
  id: ID!
  type: String!
  number: String!
  issueDate: String
  expiryDate: String
}

type Relative {
  id: ID!
  relationType: String!
  name: String!
  age: Int
}
```

* Query
```graphql
type Query {
  # /clients/{id}:
  client(id: ID!): Client

  # /clients/{id}/documents:
  documents(clientId: ID!): [Document!]!

  # /clients/{id}/relatives:
  relatives(clientId: ID!): [Relative!]!
}
```

* graphql, в принципе, позволяет вытаскивать любой набор данных ровно 1-им запросом