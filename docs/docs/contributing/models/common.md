# Common

## AuditMixIn

The `AuditMixIn` class is a mixin designed to provide quick reference auditing capabilities to SQLAlchemy models. It includes fields for tracking creation, updates, archiving, deletion, and importing of records, along with their respective timestamps and user IDs.


### Definitions

- **Created**: The state when a new entity or resource is initially instantiated or added to the system.
- **Updated**: The state when an existing entity or resource has been modified or altered in the system.
- **Archived**: The state when an entity or resource is no longer actively used but is retained for historical or reference purposes.
- **Deleted**: The state when an entity or resource is permanently removed from the system and is no longer accessible. Soft deletes will be applied and records will be retained until permanently deleted individually or by using the purge utility.

### Fields

| Field            | Type      | Description                                                                 |
|------------------|-----------|-----------------------------------------------------------------------------|
| **created_at**   | `datetime`| Timestamp when the record was created. Nullable.                          |
| 🗝️**created_by**   | `int`     | Foreign Key to `Users.ID`. ID of the user who created the record. Nullable. See [Users Model](users.md). |
| **updated_at**   | `datetime`| Timestamp when the record was last updated. Nullable.                      |
| 🗝️**updated_by**   | `int`     | Foreign Key to `Users.ID`. ID of the user who last updated the record. Nullable. See [Users Model](users.md). |
| **archived_at**  | `datetime`| Timestamp when the record was archived. Nullable.                          |
| 🗝️**archived_by**  | `int`     | Foreign Key to `Users.ID`. ID of the user who archived the record. Nullable. See [Users Model](users.md). |
| **unarchived_at**| `datetime`| Timestamp when the record was unarchived. Nullable.                        |
| 🗝️**unarchived_by**| `int`     | Foreign Key to `Users.ID`. ID of the user who unarchived the record. Nullable. See [Users Model](users.md). |
| **deleted_at**   | `datetime`| Timestamp when the record was deleted. Nullable.                           |
| 🗝️**deleted_by**   | `int`     | Foreign Key to `Users.ID`. ID of the user who deleted the record. Nullable. See [Users Model](users.md). |
| **undeleted_at** | `datetime`| Timestamp when the record was undeleted. Nullable.                         |
| 🗝️**undeleted_by** | `int`     | Foreign Key to `Users.ID`. ID of the user who undeleted the record. Nullable. See [Users Model](users.md). |
| **imported_at**  | `datetime`| Timestamp when the record was imported. Nullable.                          |
| 🗝️**imported_by**  | `int`     | Foreign Key to `Users.ID`. ID of the user who imported the record. Nullable. See [Users Model](users.md). |

### Properties

| Property      | Type      | Getter/Setter Description                                                                 |
|---------------|-----------|------------------------------------------------------------------------------------------|
| **is_archived** | `bool`   | **Getter**: Returns `True` if the record is archived (i.e., `archived_at` is not `None` and either `unarchived_at` is `None` or `archived_at` is more recent than `unarchived_at`).<br /><br />**Setter**: Sets the record as archived or unarchived. If archived, sets `archived_at` to the current UTC time and `archived_by` to `-1`. If unarchived, sets `unarchived_at` to the current UTC time and `unarchived_by` to `-1`. |
| **is_deleted** | `bool`   | **Getter**: Returns `True` if the record is deleted (i.e., `deleted_at` is not `None` and either `undeleted_at` is `None` or `deleted_at` is more recent than `undeleted_at`).<br /><br />**Setter**: Sets the record as deleted or undeleted. If deleted, sets `deleted_at` to the current UTC time and `deleted_by` to `-1`. If undeleted, sets `undeleted_at` to the current UTC time and `undeleted_by` to `-1`. |
| **is_imported** | `bool`   | **Getter**: Returns `True` if the record is imported (i.e., `imported_at` is not `None`). |

### Usage

To use the `AuditMixIn`, include it as a base class in your SQLAlchemy model. This will add the auditing fields and properties to your model, enabling you to track changes and states effectively.