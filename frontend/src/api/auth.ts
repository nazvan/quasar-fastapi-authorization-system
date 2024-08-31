import axios from 'axios';

const API_URL = 'http://localhost:8000';  // Замените на URL вашего FastAPI сервера

const axiosInstance = axios.create({
  baseURL: API_URL,
  withCredentials: true
});

export const register = async (email: string, password: string, phone_number: string, first_name: string, last_name: string) => {
  const response = await axiosInstance.post('/auth/register', { email, password, phone_number, first_name, last_name });
  return response.data;
};

export const login = async (email: string, password: string) => {
  const response = await axiosInstance.post('/auth/login', { email, password });
  return response.data;
};

export const getCurrentUser = async () => {
  try {
    console.log('Sending request to:', `${API_URL}/auth/me`);
    const response = await axiosInstance.get('/auth/me');
    console.log('Response received:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error in getCurrentUser:', error);
    throw error;
  }
};

export const logout = async () => {
  try {
    const response = await axiosInstance.post('/auth/logout/', {}, {
      headers: {
        'Content-Type': 'application/json',
      },
    });
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response) {
      console.error('Logout error:', error.response.data);
    } else {
      console.error('Unexpected error:', error);
    }
    throw error;
  }
};