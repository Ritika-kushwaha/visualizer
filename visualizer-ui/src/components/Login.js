import React, { useState } from 'react';
import axios from 'axios';

export default function Login({ onLoginSuccess, onShowRegister }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (e) => {
    // Prevent page refresh if used inside a form
    if (e) e.preventDefault(); 
    
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/login/', {
        username, 
        password
      });

      // Save the JWT "VIP Pass" and the username for the session
      localStorage.setItem('token', response.data.access);
      localStorage.setItem('username', username);
      
      onLoginSuccess();
    } catch (error) {
      // Alert the user if the server is offline or credentials fail
      alert("Login failed. Please check your credentials or server status.");
      console.error("Login Error:", error);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-6">
      <div className="w-full max-w-md bg-white rounded-[40px] shadow-2xl p-10 text-center">
        <h2 className="text-3xl font-bold text-purple-600 mb-6">Welcome Back</h2>

        <div className="space-y-4">
          <input 
            type="text" placeholder="Username" 
            className="w-full p-4 rounded-2xl bg-gray-50 border border-gray-200 outline-none focus:border-purple-500"
            onChange={(e) => setUsername(e.target.value)}
          />
          <input 
            type="password" placeholder="Password" 
            className="w-full p-4 rounded-2xl bg-gray-50 border border-gray-200 outline-none focus:border-purple-500"
            onChange={(e) => setPassword(e.target.value)}
          />
          
          <button 
            onClick={handleLogin}
            className="w-full py-4 bg-purple-600 text-white rounded-2xl font-bold text-lg hover:bg-purple-700 transition-colors shadow-lg shadow-purple-200"
          >
            SIGN IN
          </button>

          <p className="mt-8 text-center text-gray-600">
            New to ChemVisualizer? 
            <button 
              onClick={onShowRegister} 
              className="ml-2 text-purple-600 font-bold hover:underline"
            >
              Create Account
            </button>
          </p>
        </div>
      </div>
    </div>
  );
}