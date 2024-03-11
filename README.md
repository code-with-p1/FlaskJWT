<!-- Install Flask JWT -->

pip3 install Flask-JWT

<!-- Upgrade Flask-JWT -->

pip3 install --upgrade Flask-JWT

<!-- CURL to obtain a JWT token by making a POST request to the authentication endpoint of your Flask app -->

curl -X POST -H "Content-Type: application/json" -d '{"username": "user1", "password": "password1"}' http://localhost:5000/auth

<!-- CURL to access a protected route with a JWT token -->

curl -X GET -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTAwOTQ5NjUsImlhdCI6MTcxMDA5NDY2NSwibmJmIjoxNzEwMDk0NjY1LCJpZGVudGl0eSI6MX0.yWybw1nfpjqHFu8yDf4R8OTgO0tbOf89kEzTlh39_3U" http://localhost:5000/protected
