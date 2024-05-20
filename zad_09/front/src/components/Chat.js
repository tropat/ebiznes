import React, { useState } from 'react';
import axios from 'axios';

const Chat = () => {
    const [messages, setMessages] = useState([]);
    const [userQuestion, setUserQuestion] = useState('');

    const sendMessage = async () => {
        if (!userQuestion.trim()) return;

        const newMessage = { content: userQuestion };
        setMessages([...messages, newMessage]);

        try {
            const response = await axios.post('http://localhost:8000/api/chat', {
                input: userQuestion
            });

            const botMessage = { content: response.data.response };
            setMessages([...messages, newMessage, botMessage]);
        } catch (error) {
            const errorMessage = { content: `Error: ${error.message}` };
            setMessages([...messages, newMessage, errorMessage]);
        }
        setUserQuestion('');
    };

    const handleInputChange = (event) => {
        setUserQuestion(event.target.value);
    };

    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            sendMessage();
        }
    };

    return (
        <div>
            <input
                type="text"
                value={userQuestion}
                onChange={handleInputChange}
                onKeyDown={handleKeyPress}
                placeholder="Type a message"
            />
            <p>Generating a response may take a moment...</p>
            <div className="messages">
                {messages.map((msg, index) => (
                    <div key={index}>
                        {msg.content}
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Chat;
