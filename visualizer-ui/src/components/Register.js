import React, { useState } from 'react';
import axios from 'axios';
import { UserPlus, Mail, Lock, User } from 'lucide-react';

export default function Register({ onBackToLogin }) {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleRegister = async (e) => {
  e.preventDefault(); // Prevents page refresh
  setLoading(true);   // Starts the loading spinner/text
  try {
    await axios.post('http://127.0.0.1:8000/api/register/', {
      username: username,
      password: password,
      email: email
    });
    alert("Account created successfully! You can now log in.");
    onBackToLogin(); // Automatically sends them to the Login screen
  } catch (error) {
    alert("Username already exists or server is offline.");
  } finally {
    setLoading(false); // Stops the loading state
  }
};

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50 p-6">
      <div className="w-full max-w-md bg-white rounded-[40px] shadow-2xl p-10 border border-gray-100">
        <div className="flex justify-center mb-6 text-purple-600">
          <UserPlus size={48} />
        </div>
        
        <h2 className="text-3xl font-bold text-gray-800 mb-2 text-center">Join ChemVisualizer</h2>
        <p className="text-gray-500 text-center mb-8 text-sm">Create an account to start analyzing equipment data.</p>

        <form onSubmit={handleRegister} className="space-y-4">
          <div className="relative">
            <User className="absolute left-4 top-4 text-gray-400" size={20} />
            <input 
              type="text" 
              placeholder="Username" 
              required
              className="w-full p-4 pl-12 rounded-2xl bg-gray-50 border border-gray-200 outline-none focus:border-purple-500 transition-all"
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>

          <div className="relative">
            <Mail className="absolute left-4 top-4 text-gray-400" size={20} />
            <input 
              type="email" 
              placeholder="Email Address" 
              required
              className="w-full p-4 pl-12 rounded-2xl bg-gray-50 border border-gray-200 outline-none focus:border-purple-500 transition-all"
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          <div className="relative">
            <Lock className="absolute left-4 top-4 text-gray-400" size={20} />
            <input 
              type="password" 
              placeholder="Create Password" 
              required
              className="w-full p-4 pl-12 rounded-2xl bg-gray-50 border border-gray-200 outline-none focus:border-purple-500 transition-all"
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          <button 
            type="submit"
            disabled={loading}
            className="w-full py-4 bg-purple-600 text-white rounded-2xl font-bold text-lg hover:bg-purple-700 transition-all shadow-lg shadow-purple-200 disabled:opacity-50"
          >
            {loading ? "CREATING ACCOUNT..." : "CREATE ACCOUNT"}
          </button>
        </form>

        <p className="mt-8 text-center text-gray-600">
          Already have an account? 
          <button 
            onClick={onBackToLogin}
            className="ml-2 text-purple-600 font-bold hover:underline"
          >
            Sign In
          </button>
        </p>
      </div>
    </div>
  );
}