import React, { useState, useEffect } from 'react';
import { Route, Routes, useParams, useNavigate } from 'react-router-dom';
import './App.css';
import UserList from './components/UserList';
import UserDetails from './components/UserDetails';
import CreateUserForm from './components/CreateUserForm';

function UserDetailPane() {
  const { userId } = useParams();
  const [user, setUser] = useState(null);

  useEffect(() => {
    if (userId === '-1') {
      setUser({}); // Set to an empty object for create user state
      return;
    }

    fetch(`http://localhost:8000/users/${userId}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => setUser(data))
      .catch((error) => console.error('Error fetching user:', error));
  }, [userId]);

  if (userId === '-1') {
    return <CreateUserForm onSubmit={(formData) => console.log('Create user:', formData)} />;
  }

  if (!user) {
    return <div>Loading user details...</div>;
  }

  return <UserDetails userId={user.id} user={user} />;
}

// Removed the Router wrapping the App component since it is already wrapped in index.js
function App() {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const navigate = useNavigate();
  
  useEffect(() => {
    fetch('http://localhost:8000/users')
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => setUsers(data))
      .catch((error) => console.error('Error fetching users:', error));
  }, []);

  const handleUserClick = (userId) => {
    console.log('User clicked with userId:', userId);
    navigate(`/users/${userId}`, { replace: true });
  };

  const handleCreateClick = () => {
    setSelectedUser(null);
    navigate('/users/-1', { replace: true });
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

  const handleUpdateUser = (updatedUser) => {
    setUsers((prevUsers) =>
      prevUsers.map((user) => (user.id === updatedUser.id ? updatedUser : user))
    );
  };

  return (
    <div className="App">
      <div className="menu">
        <h2>Menu</h2>
        {/* Add menu items here */}
      </div>
        <div className="user-master-pane">
          <UserList
            users={users}
            onUserClick={handleUserClick}
            onCreateClick={handleCreateClick}
          />
        </div>
        <div className="user-detail-pane">
          <Routes>
            <Route path="/users/:userId" element={<UserDetailPane />} />
          </Routes>
        </div>
    </div>
  );
}

export default App;
