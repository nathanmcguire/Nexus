import React, { useState, useEffect } from 'react';
import './App.css';
import UserList from './components/UserList';
import UserDetails from './components/UserDetails';

function App() {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);

  useEffect(() => {
    fetch('/users')
      .then((response) => response.json())
      .then((data) => setUsers(data));
  }, []);

  const handleUserClick = (userId) => {
    fetch(`/users/${userId}`)
      .then((response) => response.json())
      .then((data) => setSelectedUser(data));
  };

  const handleCreateClick = () => {
    setSelectedUser(null);
  };

  const handleCreateUser = (newUser) => {
    fetch('/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newUser),
    })
      .then((response) => response.json())
      .then((createdUser) => {
        setUsers([...users, createdUser]);
        setSelectedUser(createdUser);
      });
  };

  return (
    <div className="App">
      <div className="menu">
        <h2>Menu</h2>
        {/* Add menu items here */}
      </div>
      <UserList users={users} onUserClick={handleUserClick} onCreateClick={handleCreateClick} />
      <UserDetails user={selectedUser} onCreate={handleCreateUser} />
    </div>
  );
}

export default App;
