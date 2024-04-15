import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Produkty = () => {
    const [produkty, setProdukty] = useState([]);

    useEffect(() => {
        const fetchProdukty = async () => {
            try {
                const response = await axios.get('http://localhost:8080/produkty');
                setProdukty(response.data);
            } catch (error) {
                console.error('Błąd podczas pobierania danych:', error);
            }
        };

        fetchProdukty();
    }, []);

    return (
        <div>
            <h2>Produkty</h2>
            <ul>
                {produkty.map(produkt => (
                    <li key={produkt.ID}>Produkt {produkt.Nazwa} Kategorii {produkt.KategoriaID}: {produkt.Cena} zl</li>
                ))}
            </ul>
        </div>
    );
};

export default Produkty;
