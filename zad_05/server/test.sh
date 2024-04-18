#!/bin/bash

url="http://localhost:8080"

produkt='{"Nazwa": "nowy produkt", "Cena": 20, "KategoriaID": 1}'

echo "Tworzenie nowego produktu..."
nowy_produkt=$(curl -X POST -H "Content-Type: application/json" -d "$produkt" "$url/produkty")
echo "Nowy produkt: $nowy_produkt"

id_produktu=$(echo "$nowy_produkt" | sed -n 's/.*"ID":\([0-9]*\).*/\1/p')
echo "ID nowego produktu: $id_produktu"

echo "Dodawanie produktu do koszyka..."
response=$(curl -X PUT -H "Content-Type: application/json" -d "{\"ID\": $id_produktu}" "$url/koszyk/1")
echo "Odpowiedź serwera: $response"