// import express from 'express';
// import mongoose from 'mongoose';
// import path from 'path';
// import { fileURLToPath } from 'url';
// import router from './routes/movieRouter.js';
// import cors from 'cors';

// const app = express();

// // Middleware
// app.use(cors());
// app.use(express.json());

// // API route to fetch movies
// app.use('/', router);

// // Resolve __dirname in ES Modules
// const __filename = fileURLToPath(import.meta.url);
// const __dirname = path.dirname(__filename);

// // Serve static files from the "bingeplus" directory
// app.use(express.static(path.join(__dirname, '../')));

// // Route for the root path
// app.get('/', (req, res) => {
//   res.sendFile(path.join(__dirname, '../index.html'));
// });

// // MongoDB Connection String (Your MongoDB Atlas URI)
// const mongoURI = 'mongodb+srv://bingemovies:CWuhFDboOssypOfD@binge.qvrdf.mongodb.net/BINGE';

// // Connect to MongoDB Atlas
// mongoose.connect(mongoURI, {
//   useNewUrlParser: true,
//   useUnifiedTopology: true,
// })
// .then(() => console.log('Connected to MongoDB'))
// .catch((err) => console.error('Failed to connect to MongoDB', err));

// // Start the server
// const PORT = process.env.PORT || 8080;
// app.listen(PORT, () => {
//   console.log(`Server is running on http://localhost:${PORT}`);
// });


import express from 'express';
import mongoose from 'mongoose';
import path from 'path';
import { fileURLToPath } from 'url';
import router from './routes/movieRouter.js';
import cors from 'cors';

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// API route to fetch movies
app.use('/', router);

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.use(express.static(path.join(__dirname, '../')));

// Route for the root path
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../index.html'));
});

// Start the server
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
