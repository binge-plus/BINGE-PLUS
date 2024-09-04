import express from 'express';
import mongoose from 'mongoose';
import path from 'path';
import { fileURLToPath } from 'url';
import cors from 'cors';
import Movie from './models.js';  // Import the Movie model
import router from './routes/movieRouter.js';  // Import the router

const app = express();

// Middleware
app.use(cors({
  origin: '*',
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));

app.use(express.json());

// MongoDB Connection String (Your MongoDB Atlas URI)
const mongoURI = 'mongodb+srv://bingemovies:CWuhFDboOssypOfD@binge.qvrdf.mongodb.net/BINGE';

mongoose.connect(mongoURI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log('Connected to MongoDB');
}).catch((err) => {
    console.error('MongoDB connection error:', err);
});

// Serve static HTML file
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
app.use(express.static(path.join(__dirname, '../')));

// API routes
app.use('/', router);

// Route to get 3 random movies
app.get('/api/movies/random', async (req, res) => {
    try {
        const movies = await Movie.aggregate([{ $sample: { size: 5 } }]);
        res.json(movies);
    } catch (err) {
        res.status(500).send('Server error');
    }
});

// Route for the root path
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../index.html'));
});

// Start the server
const PORT = process.env.PORT || 1111;
app.listen(PORT, () => {
  console.log(`Server is running on http://34.45.6.128:${PORT}`);
});
