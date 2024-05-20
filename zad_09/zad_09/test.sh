#!/bin/bash

url="http://localhost:8000/api/chat"

# Poprawne dane JSON
body='{"input": "can you see my message?"}'

# Użycie zmiennej $body
resp=$(curl -X POST -H "Content-Type: application/json" -d "$body" "$url")
echo "Response: $resp"
