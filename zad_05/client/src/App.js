import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Produkty from './components/Produkty';
import Koszyk from './components/Koszyk';
import Platnosci from './components/Platnosci';


const App = () => {
    const [produkty, setProdukty] = useState([]);
    const [koszyk, setKoszyk] = useState([]);
    const [formData, setFormData] = useState({});

    return (
        <Router>
            <div>
                <ul>
                    <li>
                        <Link to="/produkty">Produkty</Link>
                    </li>
                    <li>
                        <Link to="/koszyk/1">Koszyk</Link>
                    </li>
                    <li>
                        <Link to="/platnosci">Płatności</Link>
                    </li>
                </ul>
                <Routes>
                    <Route path="/produkty" element={<Produkty produkty={produkty} setProdukty={setProdukty} />} />
                    <Route path="/koszyk/1" element={<Koszyk koszyk={koszyk} setKoszyk={setKoszyk} />} />
                    <Route path="/platnosci" element={<Platnosci formData={formData} setFormData={setFormData} />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
