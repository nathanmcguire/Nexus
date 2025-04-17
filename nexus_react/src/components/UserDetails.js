import React, { useState } from 'react';

const UserDetails = ({ user, onCreate }) => {
  const [newUser, setNewUser] = useState({ username: '', password: '', is_active: true });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewUser({ ...newUser, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onCreate(newUser);
    setNewUser({ username: '', password: '', is_active: true });
  };

  if (!user) {
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

  return (
    <div className="user-details">
      <h2>User Details</h2>
      <div>
        <p>ID: {user.id}</p>
        <p>Username: {user.username}</p>
        <p>Active: {user.is_active ? 'Yes' : 'No'}</p>
      </div>
    </div>
  );
};

export default UserDetails;