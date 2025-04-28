# Audits Model

## UML Diagram
```puml
!include audits.puml
```

## Field Descriptions

- **audit_id**: A unique identifier for the audit record.
- **action**: The type of action performed (e.g., `CREATE`, `UPDATE`, `DELETE`, `READ`).
- **entity_id**: The ID of the entity being acted upon.
- **entity_type**: The type of entity being acted upon (e.g., `User`, `Order`, `Product`).
- **timestamp**: The exact time the action occurred.
- **requested_by**: A foreign key linking to the User who performed the action.
- **request_ip**: The IP address of the client making the request.
- **request_method**: The HTTP method used (e.g., `GET`, `POST`, `PUT`, `DELETE`).
- **request_url**: The URL or endpoint accessed.
- **request_payload**: The payload sent with the request (if applicable).
- **response_status**: The HTTP status code returned (e.g., `200`, `404`, `500`).
