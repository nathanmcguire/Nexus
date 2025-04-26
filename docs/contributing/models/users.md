# Users

![Users](users.puml)

## Overview
The User model is a fundamental part of the application, representing the core attributes and relationships of a user in the system. It is used across various domains and services to manage user-related data and operations.

## Definitions

The `enabled` or `disabled` state of a user determines whether the user has access to the system. This state is typically managed through the `is_active` field in the User model.

- **Enabled**: When `is_active` is set to `true`, the user account is active and can interact with the system.
- **Disabled**: When `is_active` is set to `false`, the user account is inactive and cannot access the system.

This field is crucial for managing user access without permanently deleting user data.

## Fields
The User model includes the following fields:

| Field        | Type      | Description                                                                 |
|--------------|-----------|-----------------------------------------------------------------------------|
| 🔑**id**       | Integer   |  A unique identifier for the user.                                       |
| **guid**     | UUID      | A globally unique identifier for the user.                                 |
| **username** | String    | A unique string representing the user's login name.                        |
| **password** | String    | A hashed representation of the user's password for secure storage.         |
| **enabled_at** | DateTime  | The timestamp when the user was enabled.                                |
| **enabled_by** | String    | The identifier of the user or system that enabled this user.            |
| **disabled_at**| DateTime  | The timestamp when the user was disabled.                               |
| **disabled_by**| String    | The identifier of the user or system that disabled this user.           |

For auditing-related fields (event_at, event_by), refer to the AuditMixIn model.

## Properties

| Property      | Type      | Description                                                                 |
|---------------|-----------|-----------------------------------------------------------------------------|
| **is_enabled** | `bool`   | **Getter**: Returns `True` if the user is enabled (i.e., `enabled_at` is not `None` and either `disabled_at` is `None` or `disabled_at` is earlier than `enabled_at`). |
| **password**   | `str`    | **Getter**: Returns the hashed password.<br /><br />**Setter**: Hashes the raw password using Argon2 and stores it securely.|

## Methods

| Method            | Type      | Description                                                                 |
|-------------------|-----------|-----------------------------------------------------------------------------|
| **verify_password** | `bool` | **Method**: Accepts a raw password and verifies it against the stored hashed password using Argon2. |

## Notes
- Ensure that sensitive information, such as passwords, is always stored securely using hashing algorithms like bcrypt.
- Use proper validation and constraints to maintain data integrity.
- Regularly update and audit the model to ensure it meets the application's evolving requirements.