import axios from 'axios';
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Register from "./Register";


function App() {
    return (
        <Router>
            <div>
                <Routes>
                    <Route path="/" element={<LoginPage />} />
                    <Route path="/register" element={<Register />} />
                </Routes>
            </div>
        </Router>
    );
}

function LoginPage() {
    const [username, setUsername] = React.useState('');
    const [password, setPassword] = React.useState('');
    const [info, setInfo] = React.useState('');

    const handleLogin = async () => {
        try {
            const response = await axios.post('http://localhost:3000/login', { username, password });
            setInfo(response.data.message);
        } catch (error) {
            setInfo(error.response.data.message);
        }
    };

    const handleLogout = async () => {
        try {
            await axios.post('http://localhost:3000/logout');
            setInfo('Logout successful');
        } catch (error) {
            setInfo(error.response.data.message);
        }
    };

    return (
        <div>
            Log in
            <br/>
            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />
            <br />
            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <br />
            <button onClick={handleLogin}>Login</button>
            <button onClick={handleLogout}>Logout</button>
            <p>{info}</p>
            <Link to="/register">Register</Link>
        </div>
    );
}

export default App;
