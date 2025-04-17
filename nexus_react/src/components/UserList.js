import React from 'react';

const UserList = ({ users, onUserClick, onCreateClick }) => {
  return (
    <div className="user-list">
      <h2>All Users</h2>
      <button onClick={onCreateClick} className="create-button">Create New User</button>
      <ul>
        {users.map((user) => (
          <li key={user.id} onClick={() => onUserClick(user.id)}>
            {user.username}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserList;