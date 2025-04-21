# Users

## Overview
The User model is a fundamental part of the application, representing the core attributes and relationships of a user in the system. It is used across various domains and services to manage user-related data and operations.

## Fields
The User model includes the following fields:

| Field        | Type      | Description                                                                 |
|--------------|-----------|-----------------------------------------------------------------------------|
| 🔑**id**       | Integer   |  A unique identifier for the user.                                       |
| **guid**     | UUID      | A globally unique identifier for the user.                                 |
| **username** | String    | A unique string representing the user's login name.                        |
| **password** | String    | A hashed representation of the user's password for secure storage.         |
| **is_active**| Boolean   | A flag indicating whether the user account is active.                      |

For auditing-related fields (event_at, event_by), refer to the [AuditMixIn model](../common/#auditmixin).


## Notes
- Ensure that sensitive information, such as passwords, is always stored securely using hashing algorithms like bcrypt.
- Use proper validation and constraints to maintain data integrity.
- Regularly update and audit the model to ensure it meets the application's evolving requirements.