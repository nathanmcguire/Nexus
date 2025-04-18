import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

export const fetchUsers = async () => {
  const response = await axios.get(`${API_BASE_URL}/users`);
  return response.data;
};

export const createUser = async (userData) => {
  const response = await axios.post(`${API_BASE_URL}/users`, userData);
  return response.data;
};

export const fetchUserById = async (id) => {
  console.log(`Calling API: ${API_BASE_URL}/users/${id}`);
  try {
    const response = await axios.get(`${API_BASE_URL}/users/${id}`);
    console.log('API Response:', response);
    return response.data;
  } catch (error) {
    console.error('Error in fetchUserById:', error);
    throw error;
  }
};

export const updateUser = async (id, userData) => {
  const response = await axios.patch(`${API_BASE_URL}/users/${id}`, userData);
  return response.data;
};

export const deleteUser = async (id) => {
  const response = await axios.delete(`${API_BASE_URL}/users/${id}`);
  return response.data;
};