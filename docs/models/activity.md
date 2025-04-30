# Activity Model

## UML Diagram
```puml
@startuml 
!include https://raw.githubusercontent.com/nathanmcguire/nexus/main/docs/models/activity.puml
@enduml
```

## Field Descriptions
- **id**: A unique identifier for the audit record.

- **timestamp**: The exact time the action occurred.
- **requestor_id**: A foreign key linking to the User who performed the action.
- **requestor_ip**: The IP address of the client making the request.
- **url**: The URL or endpoint accessed.
- **method**: The HTTP method used (e.g., `GET`, `POST`, `PUT`, `DELETE`).
- **payload**: The payload sent with the request (if applicable).
- **return_status**: The HTTP status code returned (e.g., `200`, `404`, `500`).

- **entity_id**: The ID of the entity being acted upon.
- **entity_type**: The type of entity being acted upon (e.g., `User`, `Order`, `Product`).

