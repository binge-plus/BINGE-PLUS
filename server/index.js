import cors from 'cors';
import express from 'express';
import router from './routes/movieRouter.js';


const app = express();
const PORT = 5555;


// Middleware
app.use(cors());
app.use(express.json());


// API route to fetch movies


app.use('/', router);

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
