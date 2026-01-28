import React, { useState } from 'react';
// Change these lines in App.js
import Login from './components/Login'; 
import Register from './components/Register';
import Dashboard from './components/Dashboard';
function App() {
  // 1. Tracks if user is logged in
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  // 2. Tracks if we should show Login or Register
  const [showRegister, setShowRegister] = useState(false);
  

  // If logged in, show the Dashboard
  // In App.js
if (isLoggedIn) {
  return <Dashboard onLogout={() => setIsLoggedIn(false)} />;
}

  // If not logged in, switch between Login and Register
  return (
    <div className="App">
      {showRegister ? (
        <Register onBackToLogin={() => setShowRegister(false)} />
      ) : (
        <Login 
          onLoginSuccess={() => setIsLoggedIn(true)} 
          onShowRegister={() => setShowRegister(true)} 
        />
      )}
    </div>
  );
}

export default App;