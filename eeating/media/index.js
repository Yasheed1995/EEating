const express = require('express');
const app = express();

const server = require('http').Server(app);
const io = require('socket.io')(server);


app.get('/', (req, res) => {
   //res.send('Hello, World!');
   res.sendFile( __dirname + '/views/index.html');
});

// there is connection
io.on('connection', (socket) => {
   console.log('Hello!');

   socket.on("greet", () => {
      socket.emit("greet", "Hi! Client.");
   });

   socket.on('diconnect', () => {
      console.log('Bye~');
   })
})


server.listen(3000, () => {
   console.log("Server Started. http://localhost:3000");
});
