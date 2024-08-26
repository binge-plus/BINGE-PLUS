import cors from 'cors';
import express from 'express';
import router from './routes/movieRouter.js';


// const app = express();
// const PORT = 8080;


// // Middleware
// app.use(cors());
// app.use(express.json());


// // API route to fetch movies


// app.use('/', router);

// // Start server
// app.listen(PORT, () => {
//     console.log(`Server is running on http://localhost:${PORT}`);
// });

const express = require('express');
const path = require('path');
const app = express();
const port = process.env.PORT || 8080;

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Handle root path
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Server is running on http://0.0.0.0:${port}`);
});
