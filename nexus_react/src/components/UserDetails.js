import React, { useState, useEffect } from 'react';
import { createUser, fetchUserById } from '../services/api';

const UserDetails = ({ userId, onCreate, onUpdate }) => {
  const [user, setUser] = useState(null);
  const [newUser, setNewUser] = useState({ username: '', password: '', is_active: true });
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    console.log('UserDetails received userId:', userId);
    if (userId) {
      const getUserDetails = async () => {
        try {
          console.log('Fetching details for userId:', userId);
          const fetchedUser = await fetchUserById(userId);
          console.log('Fetched user details:', fetchedUser);
          setUser(fetchedUser);
        } catch (error) {
          console.error('Error fetching user details:', error);
        }
      };
      getUserDetails();
    } else {
      console.log('No userId provided, resetting user state.');
      setUser(null);
    }
  }, [userId]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewUser({ ...newUser, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const createdUser = await createUser(newUser);
      onCreate(createdUser);
      setNewUser({ username: '', password: '', is_active: true });
    } catch (error) {
      console.error('Error creating user:', error);
    }
  };

  const handleEditClick = () => {
    setIsEditing(true);
  };

  const refreshUserDetails = async () => {
    if (userId) {
      try {
        const fetchedUser = await fetchUserById(userId);
        setUser(fetchedUser);
      } catch (error) {
        console.error('Error refreshing user details:', error);
      }
    }
  };

  const handleSaveClick = async () => {
    try {
      const response = await fetch(`http://localhost:8000/users/${user.id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(user),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const updatedUser = await response.json();
      console.log('User updated successfully:', updatedUser);
      setUser(updatedUser);
      setIsEditing(false);

      if (onUpdate) {
        onUpdate(updatedUser);
      }

      await refreshUserDetails();
    } catch (error) {
      console.error('Error updating user:', error);
    }
  };

  const handleArchiveClick = async () => {
    try {
      const response = await fetch(`http://localhost:8000/users/${user.id}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ is_archived: true }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      console.log('User archived successfully');
      await refreshUserDetails();
    } catch (error) {
      console.error('Error archiving user:', error);
    }
  };

  const handleDeleteClick = async () => {
    try {
      const response = await fetch(`http://localhost:8000/users/${user.id}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ is_deleted: true }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      console.log('User deleted successfully');
      await refreshUserDetails();
    } catch (error) {
      console.error('Error deleting user:', error);
    }
  };

  const handleUnarchiveClick = async () => {
    try {
      const response = await fetch(`http://localhost:8000/users/${user.id}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ is_archived: false }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const updatedUser = await response.json();
      console.log('User unarchived successfully:', updatedUser);
      setUser(updatedUser);
      await refreshUserDetails();
    } catch (error) {
      console.error('Error unarchiving user:', error);
    }
  };

  const handleUndeleteClick = async () => {
    try {
      const response = await fetch(`http://localhost:8000/users/${user.id}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ is_deleted: false }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const updatedUser = await response.json();
      console.log('User undeleted successfully:', updatedUser);
      setUser(updatedUser);
      await refreshUserDetails();
      setIsEditing(false); // Ensure the button state changes back to delete
    } catch (error) {
      console.error('Error undeleting user:', error);
    }
  };

  if (!userId) {
    return (
      <div className="user-details">
        <h2>Create New User</h2>
        <form onSubmit={handleSubmit}>
          <label>
            Username:
            <input
              type="text"
              name="username"
              value={newUser.username}
              onChange={handleInputChange}
              required
            />
          </label>
          <label>
            Password:
            <input
              type="password"
              name="password"
              value={newUser.password}
              onChange={handleInputChange}
              required
            />
          </label>
          <label>
            Active:
            <input
              type="checkbox"
              name="is_active"
              checked={newUser.is_active}
              onChange={(e) => setNewUser({ ...newUser, is_active: e.target.checked })}
            />
          </label>
          <button type="submit">Create</button>
        </form>
      </div>
    );
  }

  if (!user) {
    return <div>Loading user details...</div>;
  }

  return (
    <div className="user-details">
      <h2>User Details</h2>
      <form>
        <label>
          ID:
          <span>{user.id}</span>
        </label>
        <label>
          Username:
          <input
            type="text"
            value={user.username}
            readOnly={!isEditing}
            onChange={(e) => setUser({ ...user, username: e.target.value })}
          />
        </label>
        <label>
          Active:
          <input
            type="checkbox"
            checked={user.is_active}
            disabled={!isEditing}
            onChange={(e) => setUser({ ...user, is_active: e.target.checked })}
          />
        </label>
        {isEditing ? (
          <button type="button" onClick={handleSaveClick}>Save</button>
        ) : (
          <button type="button" onClick={handleEditClick}>Edit</button>
        )}
        {user.is_deleted ? (
          <button type="button" onClick={handleUndeleteClick}>Undelete</button>
        ) : (
          <button type="button" onClick={handleDeleteClick}>Delete</button>
        )}
        {user.is_archived ? (
          <button type="button" onClick={handleUnarchiveClick}>Unarchive</button>
        ) : (
          <button type="button" onClick={handleArchiveClick}>Archive</button>
        )}
      </form>
      {user.created_at && <p><strong>Created At:</strong> {user.created_at}</p>}
      {user.created_by && <p><strong>Created By:</strong> {user.created_by}</p>}
      {user.updated_at && <p><strong>Updated At:</strong> {user.updated_at}</p>}
      {user.updated_by && <p><strong>Updated By:</strong> {user.updated_by}</p>}
      {user.archived_at && <p><strong>Archived At:</strong> {user.archived_at}</p>}
      {user.archived_by && <p><strong>Archived By:</strong> {user.archived_by}</p>}
      {user.unarchived_at && <p><strong>Unarchived At:</strong> {user.unarchived_at}</p>}
      {user.unarchived_by && <p><strong>Unarchived By:</strong> {user.unarchived_by}</p>}
      {user.is_archived !== undefined && <p><strong>Is Archived:</strong> {user.is_archived ? 'Yes' : 'No'}</p>}
      {user.deleted_at && <p><strong>Deleted At:</strong> {user.deleted_at}</p>}
      {user.deleted_by && <p><strong>Deleted By:</strong> {user.deleted_by}</p>}
      {user.undeleted_at && <p><strong>Undeleted At:</strong> {user.undeleted_at}</p>}
      {user.undeleted_by && <p><strong>Undeleted By:</strong> {user.undeleted_by}</p>}
      {user.is_deleted !== undefined && <p><strong>Is Deleted:</strong> {user.is_deleted ? 'Yes' : 'No'}</p>}
    </div>
  );
};

export default UserDetails;