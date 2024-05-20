import React, { useState } from 'react';
import axios from 'axios';

const Chat = () => {
    const [messages, setMessages] = useState([]);
    const [userQuestion, setUserQuestion] = useState('');

    const predefinedQuestions = [
        'Hello, tell me how to make a sandwich',
        'Hello, tell me 5 ideas for a dinner',
        'Hello, how do you work?',
        'Hello, explain to me quantum mechanics',
        'Hello, tell me how computer works',

        'Thank you for your answers',
        'Thanks, goodbye',
        'It was nice to talk to you',
        'You explained a lot, thanks',
        'You were very helpful, bye'
    ];

    const sendMessage = async (messageContent) => {
        const content = messageContent || userQuestion;
        if (!content.trim()) return;

        const newMessage = { role: 'user', content: content };
        setMessages([...messages, newMessage]);

        try {
            const response = await axios.post('http://localhost:8000/api/chat', {
                input: content
            });

            const botMessage = { role: 'bot', content: response.data.response };
            setMessages([...messages, newMessage, botMessage]);
        } catch (error) {
            const errorMessage = { role: 'bot', content: `Error: ${error.message}` };
            setMessages([...messages, newMessage, errorMessage]);
        }

        setUserQuestion('');
    };

    const handleInputChange = (event) => {
        setUserQuestion(event.target.value);
    };

    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            sendMessage();
        }
    };

    const handleButtonClick = (message) => {
        sendMessage(message);
    };

    return (
        <div className="chat-container">
            <input
                type="text"
                value={userQuestion}
                onChange={handleInputChange}
                onKeyDown={handleKeyDown}
                placeholder="Type a message..."
                className="user-input"
            />
            <div className="button-container">
                {predefinedQuestions.map((msg, index) => (
                    <button key={index} onClick={() => handleButtonClick(msg)}>
                        {msg}
                    </button>
                ))}
            </div>
            <p>Generating a response may take a few moments...</p>
            <div className="messages">
                {messages.map((msg, index) => (
                    <div key={index} className={msg.role === 'user' ? 'user-message' : 'bot-message'}>
                        {msg.content}
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Chat;
