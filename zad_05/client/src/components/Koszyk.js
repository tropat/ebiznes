import React, { useEffect } from 'react';
import axios from 'axios';

const Koszyk = ({ koszyk, setKoszyk }) => {

    useEffect(() => {
        const fetchKoszyk = async () => {
            try {
                const response = await axios.get('http://localhost:8080/koszyk/1', {
                    headers: {
                        'Access-Control-Allow-Origin': '*'
                    }
                });
                setKoszyk(response.data);
            } catch (error) {
                console.error('Błąd podczas pobierania danych koszyka:', error);
            }
        };

        fetchKoszyk();
    }, []);

    return (
        <div>
            <h2>Koszyk</h2>
            <ul>
                {koszyk.Produkty && koszyk.Produkty.map(produkt => (
                    <li key={produkt.ID}>Produkt {produkt.Nazwa} Kategorii {produkt.KategoriaID}: {produkt.Cena} zl</li>
                ))}
            </ul>
        </div>
    );
};

export default Koszyk;
