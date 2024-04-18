import React, { useEffect } from 'react';
import axios from 'axios';

const Produkty = ({ produkty, setProdukty }) => {

    useEffect(() => {
        const fetchProdukty = async () => {
            try {
                const response = await axios.get('http://localhost:8080/produkty', {
                    headers: {
                        'Access-Control-Allow-Origin': '*'
                    }
                });
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
